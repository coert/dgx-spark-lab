"""General-purpose helpers shared by experiments."""

import subprocess
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from os import PathLike
from pathlib import Path


@dataclass(frozen=True, slots=True)
class CommandResult:
    """Structured outcome from a subprocess invocation."""

    command: tuple[str, ...]
    returncode: int | None
    stdout: str
    stderr: str
    timed_out: bool = False
    executable_missing: bool = False
    error: str | None = None

    @property
    def succeeded(self) -> bool:
        """Return whether the command exited successfully."""

        return (
            self.returncode == 0 and not self.timed_out and not self.executable_missing
        )


def _stream_text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode(errors="replace")
    return value


def run_command(
    command: Sequence[str],
    *,
    timeout: float = 30.0,
    cwd: str | PathLike[str] | None = None,
    env: Mapping[str, str] | None = None,
) -> CommandResult:
    """Run an argument-vector command and return its complete outcome.

    Shell parsing is never used. Missing executables and timeouts are returned
    as data rather than raised. Other operating-system errors are also captured
    in ``error``.
    """

    if isinstance(command, (str, bytes)) or not isinstance(command, Sequence):
        raise TypeError("command must be a sequence of strings")
    normalized = tuple(command)
    if not normalized or any(
        not isinstance(part, str) or not part for part in normalized
    ):
        raise ValueError("command must contain one or more non-empty strings")
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)):
        raise TypeError("timeout must be a number")
    if timeout <= 0:
        raise ValueError("timeout must be greater than zero")

    try:
        completed = subprocess.run(
            normalized,
            cwd=Path(cwd) if cwd is not None else None,
            env=dict(env) if env is not None else None,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError as exc:
        return CommandResult(
            command=normalized,
            returncode=None,
            stdout="",
            stderr="",
            executable_missing=True,
            error=str(exc),
        )
    except subprocess.TimeoutExpired as exc:
        return CommandResult(
            command=normalized,
            returncode=None,
            stdout=_stream_text(exc.stdout),
            stderr=_stream_text(exc.stderr),
            timed_out=True,
            error=f"command timed out after {timeout:g} seconds",
        )
    except OSError as exc:
        return CommandResult(
            command=normalized,
            returncode=None,
            stdout="",
            stderr="",
            error=str(exc),
        )

    return CommandResult(
        command=normalized,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )
