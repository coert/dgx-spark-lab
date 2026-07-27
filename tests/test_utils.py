"""Tests for shared subprocess helpers."""

import sys

import pytest

from common.utils import run_command


def test_run_command_captures_success() -> None:
    result = run_command((sys.executable, "-c", "print('ready')"), timeout=5)

    assert result.succeeded
    assert result.returncode == 0
    assert result.stdout == "ready\n"
    assert result.stderr == ""


def test_run_command_captures_nonzero_exit() -> None:
    result = run_command(
        (
            sys.executable,
            "-c",
            "import sys; print('bad', file=sys.stderr); raise SystemExit(3)",
        ),
        timeout=5,
    )

    assert not result.succeeded
    assert result.returncode == 3
    assert result.stderr == "bad\n"


def test_run_command_reports_missing_executable() -> None:
    result = run_command(("dgx-spark-command-that-does-not-exist",))

    assert result.executable_missing
    assert result.returncode is None
    assert result.error


def test_run_command_reports_timeout() -> None:
    result = run_command(
        (sys.executable, "-c", "import time; time.sleep(1)"), timeout=0.01
    )

    assert result.timed_out
    assert result.returncode is None
    assert result.error


@pytest.mark.parametrize("command", [(), ("",)])
def test_run_command_rejects_empty_commands(command: tuple[str, ...]) -> None:
    with pytest.raises(ValueError):
        run_command(command)


def test_run_command_rejects_string_command() -> None:
    with pytest.raises(TypeError):
        run_command("uname")
