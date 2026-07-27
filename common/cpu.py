"""Read-only access to selected Linux CPU and platform information."""

from pathlib import Path, PurePath

_ALLOWED_ROOTS = (Path("/proc"), Path("/sys"))


def read_system_file(path: str | PurePath, *, max_bytes: int = 1_048_576) -> str:
    """Read a caller-selected regular file below ``/proc`` or ``/sys``."""

    if isinstance(max_bytes, bool) or not isinstance(max_bytes, int):
        raise TypeError("max_bytes must be an integer")
    if max_bytes <= 0:
        raise ValueError("max_bytes must be greater than zero")

    candidate = Path(path)
    if not candidate.is_absolute():
        raise ValueError("path must be absolute")
    resolved = candidate.resolve(strict=True)
    if not any(resolved.is_relative_to(root) for root in _ALLOWED_ROOTS):
        raise ValueError("path must resolve below /proc or /sys")
    if not resolved.is_file():
        raise ValueError("path must identify a regular file")
    if resolved.stat().st_size > max_bytes:
        raise ValueError(f"file exceeds the {max_bytes}-byte limit")
    return resolved.read_text(encoding="utf-8", errors="replace")


def read_proc_file(relative_path: str | PurePath, **kwargs: int) -> str:
    """Read a relative path beneath ``/proc`` without writing to it."""

    relative = Path(relative_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("relative_path must stay within /proc")
    return read_system_file(Path("/proc") / relative, **kwargs)


def read_sys_file(relative_path: str | PurePath, **kwargs: int) -> str:
    """Read a relative path beneath ``/sys`` without writing to it."""

    relative = Path(relative_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("relative_path must stay within /sys")
    return read_system_file(Path("/sys") / relative, **kwargs)
