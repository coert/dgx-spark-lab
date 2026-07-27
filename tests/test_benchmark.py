"""Tests for shared benchmarking helpers."""

import pytest

from common.benchmark import benchmark_callable


def test_benchmark_callable_warms_up_and_records_iterations() -> None:
    calls: list[int] = []

    result = benchmark_callable(
        lambda: calls.append(1), warmup_iterations=2, iterations=3
    )

    assert len(calls) == 5
    assert result.iterations == 3
    assert len(result.durations_ns) == 3
    assert result.minimum_ns <= result.median_ns <= result.maximum_ns
    assert result.minimum_ns <= result.mean_ns <= result.maximum_ns
    assert result.standard_deviation_ns >= 0


@pytest.mark.parametrize(
    ("warmups", "iterations"),
    [(-1, 1), (0, 0), (True, 1), (0, False)],
)
def test_benchmark_callable_rejects_invalid_counts(
    warmups: int, iterations: int
) -> None:
    with pytest.raises(ValueError):
        benchmark_callable(
            lambda: None,
            warmup_iterations=warmups,
            iterations=iterations,
        )


def test_benchmark_callable_rejects_non_callable() -> None:
    with pytest.raises(TypeError):
        benchmark_callable(42)  # type: ignore[arg-type]
