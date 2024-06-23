"""Logical representation of a Covalent script/module."""

import importlib
import sys
from copy import deepcopy
from enum import Enum
from functools import partial
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

import covalent_cloud as cc
from covalent._workflow.electron import Electron
from covalent._workflow.lattice import Lattice, lattice
from covalent_cloud.dispatch_management.interface_functions import dispatch
from covalent_cloud.function_serve.deployment import deploy
from covalent_cloud.function_serve.service_class import FunctionService
from covalent_cloud.shared.schemas.volume import Volume
from pydantic.dataclasses import dataclass

from covalent_blueprints.reader.capture import (CapturedCloudExecutorArguments,
                                                CapturedCreateEnvArguments,
                                                CapturedDeployArguments,
                                                CapturedDispatchArguments,
                                                CapturedLatticeDeclaration,
                                                CapturedVolumeArguments,
                                                capture_cloud_calls)

_BUILDING_BLOCK_TYPES = {Electron, Lattice, FunctionService}


class ScriptType(Enum):
    """Enumerates the type of Covalent scripts in terms of the main function call"""
    DISPATCH = "dispatch"
    DEPLOY = "deploy"


@dataclass(config={"arbitrary_types_allowed": True})
class CovalentScript:
    """Represents a Covalent workflow or service scripts (.py file)"""

    electrons: Dict[str, Callable]
    services: Dict[str, FunctionService]
    lattices: List[CapturedLatticeDeclaration]
    executors: List[CapturedCloudExecutorArguments]
    dispatches: List[CapturedDispatchArguments]
    dispatch_inputs: List[Tuple]
    deploys: List[CapturedDeployArguments]
    deploy_inputs: List[Tuple]
    volumes: List[CapturedVolumeArguments]
    environments: List[CapturedCreateEnvArguments]
    source: Optional[Path] = None

    def __post_init__(self):
        self._volume_objects = {}  # Dict[str, Volume]
        self._wrapper = None  # Callable - either `cc.dispatch` or `cc.deploy`
        self._script_type = None  # ScriptType - 'dispatch' or 'deploy'

        # Validate collection and enforce assumptions.

        if len(self.dispatches) > 1:
            raise ValueError(
                "Can't convert covalent script with more than one `cc.dispatch` call."
            )
        if len(self.deploys) > 1:
            raise ValueError(
                "Can't convert covalent script with more than one `cc.deploy` call. "
                "Use a lattice to deploy multiple services inside a recipe."
            )
        if len(self.dispatches) == 1 and len(self.deploys) == 1:
            raise ValueError(
                "Can't convert covalent script with both `cc.dispatch` and `cc.deploy` calls. "
                "Consider deploying services inside the lattice."
            )
        if len(self.dispatches) == 0 and len(self.deploys) == 0:
            raise ValueError(
                "Can't convert covalent script without a `cc.dispatch` nor `cc.deploy` call."
            )

    @property
    def type(self) -> ScriptType:
        """Whether the script is a dispatch or deploy script"""
        if self._script_type is None:
            if len(self.dispatches) == 1:
                self._script_type = ScriptType.DISPATCH
            elif len(self.deploys) == 1:
                self._script_type = ScriptType.DEPLOY
            else:
                raise self._indeterminate_type_error()

        return self._script_type

    @property
    def wrapper(self) -> Callable:
        """Either `cc.dispatch` or `cc.deploy`, depending on the script"""
        if self.type == ScriptType.DISPATCH:
            if placeholder_volume := self.dispatches[0].volume:
                volume = self.get_real_volume(placeholder_volume)
            else:
                volume = None
            return partial(dispatch, volume=volume)

        if self.type == ScriptType.DEPLOY:
            if placeholder_volume := self.deploys[0].volume:
                volume = self.get_real_volume(placeholder_volume)
            else:
                volume = None
            return partial(deploy, volume=volume)

        raise self._indeterminate_type_error()

    @property
    def core_function(self) -> Callable:
        """Either the main lattice or the main function service, including post-build updates"""

        if self.type == ScriptType.DISPATCH:
            lattice_func_name = self.dispatches[0].lattice_func.__name__
            captured_lattice = next(
                captured_lattice for captured_lattice in self.lattices
                if captured_lattice._func.__name__ == lattice_func_name  # pylint: disable=protected-access
            )
            return lattice(**captured_lattice.__dict__)

        if self.type == ScriptType.DEPLOY:
            function_service = self.deploys[0].function_service
            return self.services[function_service.func_name]

        raise self._indeterminate_type_error()

    @property
    def core_function_inputs(self) -> Tuple:
        """The inputs to the main lattice or main function service"""
        if self.type == ScriptType.DISPATCH:
            return self.dispatch_inputs[0]

        if self.type == ScriptType.DEPLOY:
            return self.deploy_inputs[0]

        raise self._indeterminate_type_error()

    def get_real_volume(self, placeholder_volume: Volume) -> Volume:
        """Get the real volume object from a placeholder volume"""
        real_volume = self._volume_objects[placeholder_volume.name]

        # Update existing reference in source script.
        # Probably not necessary, but might as well...
        placeholder_volume.__dict__ = real_volume.__dict__.copy()

        return real_volume

    def get_cloud_executable(self, *args, **kwargs) -> Callable:
        """Either `cc.dispatch(core_lattice)` or `cc.deploy(core_service)`"""
        func = deepcopy(self.core_function)

        if isinstance(func, Lattice):
            self._custom_build_graph(func, *args, **kwargs)

        return self.wrapper(func)

    def create_envs(self, wait: bool = True) -> None:
        """Create the environments used in the script"""
        for env in self.environments:
            kwargs = env.__dict__.copy()
            kwargs["wait"] = wait
            cc.create_env(**kwargs)

    def create_volumes(self) -> None:
        """Create the volumes used in the script"""
        for volume in self.volumes:
            volume_obj = cc.volume(**volume.__dict__)
            self._volume_objects[volume.name] = volume_obj

    @classmethod
    def from_module(cls, module_name: str) -> 'CovalentScript':
        """Convert a module (covalent script) into a `CovalentScript` object"""
        with capture_cloud_calls() as script_data:
            if module_name not in sys.modules:
                module = importlib.import_module(module_name)
            else:
                module = importlib.reload(sys.modules[module_name])

        electrons, services = CovalentScript._read(module)

        return cls(
            electrons=electrons,
            services=services,
            **script_data
        )

    def _indeterminate_type_error(self) -> RuntimeError:
        return RuntimeError(
            "Can't determine whether to dispatch or deploy script."
        )

    def _custom_build_graph(self, lattice_: Lattice, *args, **kwargs) -> None:
        # pylint: disable=protected-access

        lattice_.build_graph(*args, **kwargs)

        # Map of electron names to updated metadata.
        electron_metadata_dict = {
            name: electron.electron_object.metadata.copy()  # type: ignore
            for name, electron in self.electrons.items()
        }

        # Map of task group IDs to updated metadata.
        electron_task_groups = {}

        # Identify electron task groups and prepare metadata for them.
        for node_id in lattice_.transport_graph._graph.nodes:
            node_dict = lattice_.transport_graph._graph.nodes[node_id]
            name = node_dict["name"]

            if new_metadata := electron_metadata_dict.get(name):

                # Prepare metadata for the electron's task group.
                task_group_id = node_dict["task_group_id"]
                electron_task_groups[task_group_id] = new_metadata["executor_data"]

                # Shorten loop to avoid redundant iterations.
                del electron_metadata_dict[name]

            # Exit once all electrons have been processed.
            if not electron_metadata_dict:
                break

        # Loop again to set metadata for task groups.
        for node_id in lattice_.transport_graph._graph.nodes:
            node_dict = lattice_.transport_graph._graph.nodes[node_id]
            task_group_id = node_dict["task_group_id"]

            if task_group_id in electron_task_groups:

                # Set the electron's executor for tasks in its task group.
                node_dict["metadata"]["executor_data"] = electron_task_groups[task_group_id]

        # Nullify .build_graph() to prevent re-build during dispatch.
        setattr(lattice_, "build_graph", lambda *_, **__: None)

    @staticmethod
    def _read(module) -> Tuple[dict, dict]:
        """Extract any electrons or services from the module.
        Must call inside `capture_cloud_calls` context to avoid initializing
        real cloud resources."""

        def _get_callable_type(func):
            return Electron if hasattr(func, "electron_object") else type(func)

        electrons = {}
        services = {}

        # Collect covalent objects.
        for obj_name, obj in module.__dict__.items():

            # Check each object.
            if not callable(obj):
                continue
            if (type_ := _get_callable_type(obj)) not in _BUILDING_BLOCK_TYPES:
                continue

            # Sort each object.
            if type_ is Electron:
                electrons[obj_name] = obj

            elif type_ is FunctionService:
                services[obj_name] = obj

        return electrons, services
