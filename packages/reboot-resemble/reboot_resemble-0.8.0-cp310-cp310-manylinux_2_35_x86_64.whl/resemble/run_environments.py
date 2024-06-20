import os
from enum import Enum
from resemble.settings import (
    ENVVAR_KUBERNETES_SERVICE_HOST,
    ENVVAR_RSM_DEV,
    ENVVAR_RSM_SERVE,
)


class RunEnvironment(Enum):
    """Known run environments."""
    RSM_DEV = 1
    RSM_SERVE = 2
    KUBERNETES = 3


class InvalidRunEnvironment(RuntimeError):
    """Exception for when run environment cannot be determined."""
    pass


def _detect_run_environment() -> RunEnvironment:
    """Internal helper to determine what run environment we are in."""
    if os.environ.get(ENVVAR_RSM_DEV, 'false').lower() == 'true':
        return RunEnvironment.RSM_DEV
    elif os.environ.get(ENVVAR_RSM_SERVE, 'false').lower() == 'true':
        return RunEnvironment.RSM_SERVE
    elif os.environ.get(ENVVAR_KUBERNETES_SERVICE_HOST) is not None:
        return RunEnvironment.KUBERNETES

    raise InvalidRunEnvironment()


def on_kubernetes() -> bool:
    """Helper for checking if we are running in a Kubernetes
    cluster."""
    try:
        return _detect_run_environment() == RunEnvironment.KUBERNETES
    except InvalidRunEnvironment:
        return False
