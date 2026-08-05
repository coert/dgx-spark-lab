# Distributed Inference

This track builds a reproducible progression from a single-node inference
baseline to two-node tensor-parallel inference.

## Notebook sequence

1. `00-environment-and-model-baseline.ipynb` — verify software, nodes, model
   metadata, and benchmark definitions.
2. `01-single-node-inference.ipynb` — establish the single-node latency,
   throughput, memory, and correctness baseline.
3. `02-tensor-parallel-launch.ipynb` — launch the smallest valid two-node
   tensor-parallel configuration and verify rank participation.
4. `03-tensor-parallel-scaling.ipynb` — compare single-node and two-node
   execution under controlled workloads.
5. `04-prefill-and-decode.ipynb` — separate prompt prefill from autoregressive
   decode behavior.
6. `05-batching-and-concurrency.ipynb` — study batching, request concurrency,
   queueing, latency, and throughput.
7. `06-communication-profiling.ipynb` — relate distributed execution to NCCL,
   network traffic, synchronization, and communication phases.
8. `07-summary.ipynb` — synthesize verified findings and identify follow-up
   experiments.

## Launching the notebooks

From the repository root, synchronize the environment and start JupyterLab:

```bash
uv sync
uv run jupyter lab
```

Before distributed measurements, both nodes must use the same repository
revision, environment, model artifacts, and compatible configuration.

Advertised link rate, GPU utilization, and successful process startup are not
substitutes for measured inference performance. The direct connections are two
100 Gb/s links, but their existence does not establish that a workload uses or
aggregates both rails.

## Experimental discipline

Write a falsifiable prediction before each experiment. Keep predictions,
measurements, observations, explanations, and unresolved questions distinct.
Measured facts must come from actual saved outputs; derived values and
architectural inference must be labeled separately.
