"""Safe, lazy CUDA discovery through PyTorch."""

from dataclasses import dataclass
from importlib import import_module
from typing import Any


@dataclass(frozen=True, slots=True)
class CudaInfo:
    """CUDA availability information reported by an optional PyTorch install."""

    torch_installed: bool
    available: bool
    device_count: int
    device_names: tuple[str, ...]
    torch_version: str | None = None
    cuda_version: str | None = None
    error: str | None = None


def detect_cuda() -> CudaInfo:
    """Detect CUDA without importing PyTorch until this function is called."""

    try:
        torch: Any = import_module("torch")
    except ModuleNotFoundError:
        return CudaInfo(False, False, 0, ())
    except Exception as exc:  # PyTorch may fail while loading native libraries.
        return CudaInfo(False, False, 0, (), error=str(exc))

    try:
        available = bool(torch.cuda.is_available())
        device_count = int(torch.cuda.device_count()) if available else 0
        names = tuple(
            str(torch.cuda.get_device_name(index)) for index in range(device_count)
        )
        return CudaInfo(
            torch_installed=True,
            available=available,
            device_count=device_count,
            device_names=names,
            torch_version=str(torch.__version__),
            cuda_version=(
                str(torch.version.cuda) if torch.version.cuda is not None else None
            ),
        )
    except Exception as exc:
        return CudaInfo(
            torch_installed=True,
            available=False,
            device_count=0,
            device_names=(),
            torch_version=str(getattr(torch, "__version__", "unknown")),
            error=str(exc),
        )
