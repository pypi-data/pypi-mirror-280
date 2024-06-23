"""Module for capturing essential elements from Covalent scripts."""

import contextlib
from datetime import timedelta
from typing import Any, Callable, Dict, List, Optional, Union
from unittest.mock import MagicMock, patch

import covalent_cloud as cc
from covalent_cloud.function_serve.service_class import FunctionService
from covalent_cloud.shared.classes.settings import Settings, settings
from covalent_cloud.shared.schemas.volume import Volume
from pydantic.dataclasses import Field, dataclass

CreateEnvCondaArgs = Optional[Union[str, List[str], Dict[str, List[str]]]]


@dataclass
class CapturedCreateEnvArguments:
    """Arguments captured from `cc.create_env()` calls"""
    name: str
    pip: Optional[Union[str, List[str]]] = Field(default_factory=list)
    conda: CreateEnvCondaArgs = Field(default_factory=list)
    variables: Optional[List] = None
    settings: Optional[Settings] = settings
    wait: Optional[bool] = False
    timeout: Optional[int] = 1800
    base_image: Optional[str] = None


@dataclass
class CapturedVolumeArguments:
    """Arguments captured from `cc.volume()` calls"""
    name: str
    vtype: Optional[str] = "OBJECT_STORAGE"
    settings: Optional[Settings] = settings


@dataclass(config={"arbitrary_types_allowed": True})
class CapturedLatticeDeclaration:
    """Arguments captures from `ct.lattice()` calls"""
    _func: Callable
    backend: Optional[str] = None
    executor: Optional[Any] = None
    workflow_executor: Optional[Any] = None
    deps_bash: Optional[Any] = None
    deps_pip: Optional[Any] = None
    call_before: Optional[Any] = None
    call_after: Optional[Any] = None
    triggers: Optional[Any] = None


@dataclass(config={"arbitrary_types_allowed": True})
class CapturedDispatchArguments:
    """Arguments captured from `cc.dispatch()` calls"""
    lattice_func: Callable
    settings: Settings = settings
    volume: Union[Volume, None] = None


@dataclass(config={"arbitrary_types_allowed": True})
class CapturedDeployArguments:
    """Arguments captured from `cc.deploy()` calls"""
    function_service: FunctionService
    volume: Optional[Volume] = None


@dataclass
class CapturedCloudExecutorArguments:
    """Arguments captured from `cc.CloudExecutor()` instantiations"""
    num_cpus: int = 1
    memory: Union[int, str] = 1024
    num_gpus: int = 0
    gpu_type: Union[str, cc.cloud_executor.GPU_TYPE] = ""
    env: str = "default"
    time_limit: Union[int, timedelta, str] = 60 * 30
    volume_id: Optional[int] = None
    settings: Dict = Field(default_factory=settings.model_dump)
    validate_environment: bool = True


@contextlib.contextmanager
def capture_cloud_calls():
    """Context designed to capture Covalent function calls and objects instantiations,
    when a script is imported inside it"""

    # pylint: disable=import-outside-toplevel
    from covalent_cloud.cloud_executor.cloud_executor import \
        CloudExecutor as CE

    class _Result:
        """Mock result object to patch typical manipulations."""
        # pylint: disable=missing-function-docstring
        @property
        def result(self):
            return self

        @property
        def value(self):
            return None

        def load(self):
            return self

    class _Deployment:
        """"Mock deployment object to patch typical manipulations."""
        # pylint: disable=too-few-public-methods

        def __getattribute__(self, name: str) -> None:
            return None

    script_data = {
        "environments": [],
        "volumes": [],
        "lattices": [],
        "dispatches": [],
        "deploys": [],
        "dispatch_inputs": [],
        "deploy_inputs": [],
        "executors": [],
    }

    def _capture_create_env(*args, **kwargs):
        script_data["environments"].append(
            CapturedCreateEnvArguments(*args, **kwargs)
        )

    def _capture_volume(*args, **kwargs):
        script_data["volumes"].append(CapturedVolumeArguments(*args, **kwargs))
        name = kwargs.get("name") or args[0]

        # Return a placeholder to be assigned wherever applicable.
        # The assigned name is used to create the real volume later on.
        placeholder_volume = Volume(name=name, id=-1, user_id="")
        return placeholder_volume

    def _capture_lattice_declaration(_func=None, **kwargs):
        def _capture_lattice_wrapper(_func=None):
            script_data["lattices"].append(
                CapturedLatticeDeclaration(_func=_func, **kwargs)
            )
            return _func

        if _func is None:
            return _capture_lattice_wrapper
        return _capture_lattice_wrapper(_func)

    def _capture_dispatch(*args, **kwargs):
        script_data["dispatches"].append(
            CapturedDispatchArguments(*args, **kwargs)
        )
        return lambda *a, **k: script_data["dispatch_inputs"].append((a, k))

    def _capture_deploy_inputs(*a, **k):
        script_data["deploy_inputs"].append((a, k))
        return _Deployment()

    def _capture_deploy(*args, **kwargs):
        script_data["deploys"].append(CapturedDeployArguments(*args, **kwargs))
        return _capture_deploy_inputs

    def _capture_cloud_executor(*args, **kwargs):
        script_data["executors"].append(
            CapturedCloudExecutorArguments(*args, **kwargs)
        )
        kwargs["validate_environment"] = False
        return CE(*args, **kwargs)

    def _error_on_os_dispatch(*_, **__):
        raise ValueError(
            "Detected use of `ct.dispatch`. Please replace with `cc.dispatch`"
        )

    with (
        # Handled functions.
        patch("covalent_cloud.create_env", _capture_create_env),
        patch("covalent_cloud.volume", _capture_volume),
        patch("covalent.lattice", _capture_lattice_declaration),
        patch("covalent_cloud.dispatch", _capture_dispatch),
        patch("covalent_cloud.deploy", _capture_deploy),
        patch("covalent_cloud.CloudExecutor", _capture_cloud_executor),

        # Disabled functions.
        patch("covalent_cloud.get_deployment", lambda *_, **__: _Deployment()),
        patch("covalent_cloud.get_result", lambda *_, **__: _Result()),
        patch("covalent_cloud.save_api_key", lambda *_, **__: None),
        patch("builtins.print", MagicMock()),

        # Error conditions.
        patch("covalent.dispatch", _error_on_os_dispatch),
    ):
        yield script_data
