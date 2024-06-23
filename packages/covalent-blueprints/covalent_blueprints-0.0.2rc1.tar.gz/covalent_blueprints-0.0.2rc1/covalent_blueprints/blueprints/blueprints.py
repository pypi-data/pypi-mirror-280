"""Implementation of the main blueprint object."""

import os
import warnings
from typing import Any, Dict, Generic, List, Tuple, Type, TypeVar, Union

from covalent._results_manager.result import Result
from covalent._shared_files.context_managers import active_lattice_manager
from covalent._workflow.electron import Electron, electron
from covalent_cloud.dispatch_management.interface_functions import get_result
from covalent_cloud.function_serve.deployment import Deployment, get_deployment
from covalent_cloud.service_account_interface.auth_config_manager import \
    get_api_key

from covalent_blueprints.blueprints.executor_map import ExecutorMap
from covalent_blueprints.blueprints.inputs import BlueprintInputs
from covalent_blueprints.blueprints.summary import BlueprintSummary
from covalent_blueprints.reader.script import CovalentScript, ScriptType

API_KEY_ENV_VAR = "CC_API_KEY"

MISSING_API_KEY_MESSAGE = f"""
Covalent Cloud API key is not set. Please copy your API key from the Covalent Cloud Dashboard and either run:

    >>> from covalent_blueprints import save_api_key
    >>> save_api_key("<you-api-key>")

or set the environment variable in your shell:

    $ export {API_KEY_ENV_VAR}="<your-api-key>".

Note that the environment variable will override any saved API key.
""".strip()

CALL_OUTSIDE_ACTIVE_LATTICE_WARNING = """Attempted to run blueprint locally.

This can lead to unexpected behavior and is not generally recommended for the
high-level blueprints interface. Use the blueprint's `.run()` method to execute
it in the cloud or call it inside a lattice to run it as part of a larger workflow.

Set this blueprints `.call_warning` attribute to False to disable this warning.
"""


M = TypeVar("M", bound=ExecutorMap)


class CovalentBlueprint(Generic[M]):
    """A runnable blueprint that represents a Covalent workflow or service."""

    executor_map_type: Type = ExecutorMap

    @classmethod
    def create_executor_map(cls, script: CovalentScript) -> M:
        """Create an executor map for this blueprint"""
        return cls.executor_map_type(script)

    def __init__(self, name: str, script: CovalentScript, executor_map: M):
        self._name = name
        self._script = script
        self._inputs = BlueprintInputs(script)
        self._executors = executor_map
        self._ids: List[Tuple[str, str]] = []

        # Warn when calling the blueprint directly outside of a lattice
        self.call_warning = True

    @property
    def name(self) -> str:
        """Name of the original Covalent script"""
        return self._name

    @property
    def executors(self) -> M:
        """A map from electron/service names to corresponding executors"""
        return self._executors

    @property
    def environments(self) -> List[Dict[str, Any]]:
        """A map from environment names to corresponding environment strings"""
        return [
            {k: v for k, v in env.__dict__.items() if k != "settings"}
            for env in self._script.environments
        ]

    @property
    def volumes(self) -> List[Dict[str, Any]]:
        """A map from volume names to corresponding volume strings"""
        omit_keys = ["settings", "vtype"]
        return [
            {k: v for k, v in volume.__dict__.items() if k not in omit_keys}
            for volume in self._script.volumes
        ]

    @property
    def inputs(self) -> BlueprintInputs:
        """Inputs to the blueprint"""
        return self._inputs

    @property
    def ids(self) -> List[Tuple[str, str]]:
        """Dispatch and/or function IDs of workflow results and/or deployments."""
        return self._ids.copy()

    def set_default_inputs(self, *args, **kwargs) -> None:
        """Call this method with any args/kwargs to set the default inputs for the blueprint.
        Args and kwargs can be set separately or together.
        """
        if len(args) != 0:
            self.inputs.args = args
        if len(kwargs) != 0:
            self.inputs.kwargs = kwargs

    def _check_api_key(self) -> None:
        api_key = os.getenv("CC_API_KEY") or get_api_key()
        if not api_key:
            raise ValueError(MISSING_API_KEY_MESSAGE)

    def _rebuild(self) -> None:
        """Rebuild blueprint components by modifying tasks and services in place"""
        executors_dict = self._executors.map

        # Electrons
        for electron_name, electron_ in self._script.electrons.items():
            # Create replacement electron.
            new_executor = executors_dict[electron_name]
            new_electron = electron(electron_, executor=new_executor)

            # Update object data; used to update the transport graph at runtime.
            electron_.electron_object = new_electron.electron_object  # type: ignore

        # Services
        for service_name, service in self._script.services.items():
            service.executor = executors_dict[service_name]
            if placeholder_volume := service.volume:
                service.volume = self._script.get_real_volume(
                    placeholder_volume
                )

    def create_envs(self) -> None:
        """Create the environments used in this blueprint"""
        self._script.create_envs()

    def create_volumes(self) -> None:
        """Create the volumes used in this blueprint"""
        self._script.create_volumes()

    def build(self) -> None:
        """Prepare the blueprint for execution"""
        self._check_api_key()  # API key is required for envs and volumes
        self.create_envs()
        self.create_volumes()
        self._rebuild()

    def run(self, *args, wait_for_result: bool = True, **kwargs) -> Union[str, Result, Deployment]:
        """Run the underlying workflow dispatch or service deployment in the cloud.
        Positional and keyword arguments override the default inputs set in the blueprint.

        Args:
            wait_for_result: Wait for the workflow to complete or the deployment
                             to reach an active state. Set to False to run asynchronously.
                             Defaults to True.

        Returns:
            If wait_for_result is True, the workflow result or deployment client is returned.
            Otherwise, the workflow dispatch ID or a not-yet-active deployment client is returned.
            Use `cc.get_result` or `cc.get_deployment` with `wait=True` to retrieve the final
            result or active deployment.
        """
        self.build()
        args, kwargs = self.inputs.override_defaults(args, kwargs)

        # Execute
        cloud_executable = self._script.get_cloud_executable(*args, **kwargs)
        handle = cloud_executable(*args, **kwargs)

        # Record the dispatch or deployment ID
        id_ = handle.function_id if isinstance(handle, Deployment) else handle
        self._ids.append((self._script.type.value, id_))

        if not wait_for_result:
            return handle

        if self._script.type == ScriptType.DISPATCH:
            res = get_result(handle, wait=True)
            res.result.load()
            return res.result.value
        if self._script.type == ScriptType.DEPLOY:
            return get_deployment(handle, wait=True)

        raise ValueError("Unknown type of cloud executable")

    def __call__(self, *args, **kwargs) -> Electron:
        """Run the blueprint as an electron or sub-lattice. This method does not
        run the blueprint in the cloud, unless it is used inside a lattice.
        """

        if (self.call_warning and active_lattice_manager.get_active_lattice() is None):
            warnings.warn(CALL_OUTSIDE_ACTIVE_LATTICE_WARNING, stacklevel=2)

        self.build()
        args, kwargs = self.inputs.override_defaults(args, kwargs)

        # Execute inside a lattice -- i.e. return an electron.
        core_function = self._script.core_function

        if self._script.type == ScriptType.DISPATCH:
            executor = core_function.get_metadata("executor")  # type: ignore
            return electron(core_function, executor=executor)(*args, **kwargs)

        if self._script.type == ScriptType.DEPLOY:
            return core_function(*args, **kwargs)

        raise ValueError("Unknown type of cloud executable")

    def summary(self, get_source: bool = False) -> Dict[str, Any]:
        """Get a summary of the blueprint.

        Args:
            get_source: Include the content of the source file. Defaults to False.

        Returns:
            A dictionary with the blueprint summary.
        """
        summary_ = BlueprintSummary(
            name=self.name,
            type=self._script.type.value,
            inputs=self.inputs.to_dict(),
            executors={k: v.__dict__ for k, v in self.executors.map.items()},
            environments=self.environments,
            volumes=[volume["name"] for volume in self.volumes],
            source_file=self._script.source,
        )
        if get_source:
            summary_.get_source()

        return summary_.model_dump()
