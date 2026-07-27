#!/usr/bin/env python3

"""Create a basic benchmark plot from a CSV file."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot one numeric benchmark column against another."
    )
    parser.add_argument("csv", type=Path, help="Input CSV file")
    parser.add_argument("--x", required=True, help="Column for the x-axis")
    parser.add_argument("--y", required=True, help="Column for the y-axis")
    parser.add_argument("--title", default=None, help="Optional chart title")
    parser.add_argument("--output", type=Path, required=True, help="Output image")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.csv.is_file():
        raise SystemExit(f"Input file does not exist: {args.csv}")

    dataframe = pd.read_csv(args.csv)

    missing = [name for name in (args.x, args.y) if name not in dataframe.columns]
    if missing:
        available = ", ".join(str(column) for column in dataframe.columns)
        raise SystemExit(
            f"Missing column(s): {', '.join(missing)}. Available: {available}"
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots()
    axis.plot(dataframe[args.x], dataframe[args.y], marker="o")
    axis.set_xlabel(args.x)
    axis.set_ylabel(args.y)
    axis.set_title(args.title or f"{args.y} by {args.x}")
    axis.grid(True)
    figure.tight_layout()
    figure.savefig(args.output, dpi=160)


if __name__ == "__main__":
    main()
