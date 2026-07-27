# Experiment: <name>

## Question

What are we trying to determine?

## Hypothesis

What result do we expect, and why?

## Hardware topology

- Head node:
- Worker node:
- GPU placement:
- Network rail or rails:
- Parallelism strategy:

## Software

- Repository commit:
- Container image:
- Python:
- CUDA:
- PyTorch:
- NCCL:
- Other relevant packages:

## Configuration

Record all relevant command-line arguments and environment variables.

~~~bash
# Example command
~~~

## Procedure

List every step required to reproduce the experiment.

1. Prepare the environment.
2. Start the required services.
3. Run the benchmark.
4. Collect the results.
5. Stop and clean up the environment.

## Measurements

- Throughput
- Latency
- GPU utilization
- CPU utilization
- Memory consumption
- Network throughput
- Error rate or numerical correctness

## Results

Reference machine-readable files under `results/raw/`.

| Measurement | Result |
|---|---:|
| Example | 0 |

## Analysis

Explain the observations, bottlenecks, anomalies, and relevant trade-offs.

## Conclusion

State what was learned and which experiment should follow.
