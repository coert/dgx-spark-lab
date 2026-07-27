"""Minimal plotting helpers with an optional Matplotlib dependency."""

from collections.abc import Iterable
from typing import Any


def plot_timings(
    durations_ns: Iterable[int],
    *,
    ax: Any = None,
    label: str | None = None,
    **plot_kwargs: Any,
) -> Any:
    """Plot timing samples in milliseconds and return the Matplotlib axes."""

    from matplotlib import pyplot as plt

    axes = ax if ax is not None else plt.subplots()[1]
    values_ms = [duration / 1_000_000 for duration in durations_ns]
    axes.plot(range(1, len(values_ms) + 1), values_ms, label=label, **plot_kwargs)
    axes.set_xlabel("Iteration")
    axes.set_ylabel("Elapsed time (ms)")
    return axes


def histogram_timings(
    durations_ns: Iterable[int],
    *,
    ax: Any = None,
    **hist_kwargs: Any,
) -> Any:
    """Plot a histogram of timing samples in milliseconds."""

    from matplotlib import pyplot as plt

    axes = ax if ax is not None else plt.subplots()[1]
    values_ms = [duration / 1_000_000 for duration in durations_ns]
    axes.hist(values_ms, **hist_kwargs)
    axes.set_xlabel("Elapsed time (ms)")
    axes.set_ylabel("Count")
    return axes
