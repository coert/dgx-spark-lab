"""Small, dependency-free benchmarking primitives."""

from collections.abc import Callable
from dataclasses import dataclass
from statistics import fmean, median, pstdev
from time import perf_counter_ns
from typing import Any


@dataclass(frozen=True, slots=True)
class BenchmarkResult:
    """Summary of repeated wall-clock measurements in nanoseconds."""

    iterations: int
    durations_ns: tuple[int, ...]
    minimum_ns: int
    maximum_ns: int
    mean_ns: float
    median_ns: float
    standard_deviation_ns: float


def _validate_iteration_count(name: str, value: int, *, allow_zero: bool) -> None:
    minimum = 0 if allow_zero else 1
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        qualifier = "non-negative" if allow_zero else "positive"
        raise ValueError(f"{name} must be a {qualifier} integer")


def benchmark_callable[T](
    function: Callable[..., T],
    *args: Any,
    warmup_iterations: int = 1,
    iterations: int = 10,
    **kwargs: Any,
) -> BenchmarkResult:
    """Warm up and repeatedly time a callable.

    The callable's return values are intentionally discarded. Timings use
    :func:`time.perf_counter_ns` and describe elapsed wall-clock time.
    """

    if not callable(function):
        raise TypeError("function must be callable")
    _validate_iteration_count("warmup_iterations", warmup_iterations, allow_zero=True)
    _validate_iteration_count("iterations", iterations, allow_zero=False)

    for _ in range(warmup_iterations):
        function(*args, **kwargs)

    durations: list[int] = []
    for _ in range(iterations):
        start_ns = perf_counter_ns()
        function(*args, **kwargs)
        durations.append(perf_counter_ns() - start_ns)

    durations_ns = tuple(durations)
    return BenchmarkResult(
        iterations=iterations,
        durations_ns=durations_ns,
        minimum_ns=min(durations_ns),
        maximum_ns=max(durations_ns),
        mean_ns=fmean(durations_ns),
        median_ns=median(durations_ns),
        standard_deviation_ns=pstdev(durations_ns),
    )
