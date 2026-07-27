# DGX Spark Lab

Experiments on two NVIDIA DGX Spark systems connected by two direct
100 Gb/s ConnectX/RDMA links.

## Nodes

| Node | Rail 0 | Rail 1 |
|---|---|---|
| spark-0240 | 10.200.0.1 | 10.201.0.1 |
| spark-f868 | 10.200.0.2 | 10.201.0.2 |

## Research tracks

1. Distributed inference
2. Network and NCCL benchmarks
3. Distributed training
4. Mixture of Experts
5. GPUDirect RDMA
6. NVSHMEM
7. GPU vector search
8. Speech pipelines
9. Multimodal pipelines
10. Cluster scheduling

## Setup

~~~bash
uv sync
make check
~~~

## Reproducibility

Before running an important experiment:

~~~bash
make system-info
~~~

Store machine-readable benchmark results under `results/raw/`.

Generated summaries, plots, and tables belong under `results/processed/`.

Large model weights, checkpoints, profiler captures, and other generated
artifacts are intentionally excluded from Git.
