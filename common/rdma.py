"""Discovery helpers for common RDMA command-line utilities."""

from dataclasses import dataclass
from shutil import which

from common.utils import CommandResult, run_command

RDMA_UTILITIES = ("ibv_devices", "ibstat", "rdma")


@dataclass(frozen=True, slots=True)
class RdmaUtility:
    """Location and availability of an RDMA utility."""

    name: str
    path: str | None

    @property
    def available(self) -> bool:
        """Return whether the executable was found on PATH."""

        return self.path is not None


def detect_rdma_utilities() -> tuple[RdmaUtility, ...]:
    """Locate common RDMA utilities without executing them."""

    return tuple(RdmaUtility(name, which(name)) for name in RDMA_UTILITIES)


def run_rdma_utility(
    name: str, *arguments: str, timeout: float = 30.0
) -> CommandResult:
    """Explicitly execute one supported RDMA utility."""

    if name not in RDMA_UTILITIES:
        supported = ", ".join(RDMA_UTILITIES)
        raise ValueError(f"unsupported RDMA utility; choose one of: {supported}")
    return run_command((name, *arguments), timeout=timeout)
