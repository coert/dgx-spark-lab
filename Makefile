SHELL := /usr/bin/env bash

.PHONY: help sync check system-info lint format test status

help:
	@printf '%s\n' \
	  'make sync         Sync root Python environment' \
	  'make check        Check both DGX Spark nodes' \
	  'make system-info  Capture reproducibility information' \
	  'make lint         Run Ruff and mypy' \
	  'make format       Format Python code' \
	  'make test         Run tests' \
	  'make status       Show Git and cluster status'

sync:
	uv sync

check:
	./scripts/check-cluster.sh

system-info:
	./scripts/capture-system-info.sh

lint:
	uv run ruff check .
	uv run mypy .

format:
	uv run ruff format .
	uv run ruff check --fix .

test:
	uv run pytest

status:
	@echo '=== Git ==='
	@git status --short --branch
	@echo
	@echo '=== Cluster ==='
	@./scripts/check-cluster.sh
