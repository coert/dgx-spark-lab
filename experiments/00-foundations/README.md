# Foundations

These labs build the systems foundations needed to reason about performance on
the DGX Spark: CPU execution, memory behavior, CUDA, profiling, and RDMA. Each
notebook is a structured experiment template, not a source of pre-recorded
hardware claims.

## Notebook sequence

1. `00-machine-overview.ipynb` — inspect the host, GPU, storage, and network
   baseline.
2. `01-cpu-architecture.ipynb` — examine CPU topology and heterogeneous cores.
3. `02-memory-hierarchy.ipynb` — explore cache and main-memory behavior.
4. `03-linux-memory.ipynb` — connect Linux memory reporting to process behavior.
5. `04-vectorization.ipynb` — study data-parallel CPU execution.
6. `05-cuda-fundamentals.ipynb` — establish the CUDA execution model.
7. `06-gpu-memory.ipynb` — compare GPU memory access and transfer behavior.
8. `07-cuda-streams.ipynb` — investigate asynchronous work and overlap.
9. `08-profiling.ipynb` — practice measurement with profiling tools.
10. `09-rdma-fundamentals.ipynb` — inspect RDMA devices and concepts safely.
11. `10-summary.ipynb` — connect the results and identify follow-up work.

## Launching the notebooks

From the repository root, synchronize the environment and start JupyterLab:

```bash
uv sync
uv run jupyter lab
```

Opening JupyterLab from the repository root also makes the root-level `common`
package available naturally. The notebooks include a small repository-root
check so that the same imports work when an editor chooses a different working
directory.

In VS Code, open this repository as the workspace, open a notebook, choose
**Select Kernel**, then select **Python Environments** and the interpreter at
`.venv/bin/python`. If it is not listed, use **Enter interpreter path** and
select that file explicitly.

## Experimental discipline

Write the prediction before running the experiment. A prediction makes the
assumptions testable and reduces the temptation to explain a result after the
fact.

Only record observations produced by an actual run on an identified system.
Keep expected properties, measured observations, and explanations distinct;
never copy expected values into the observations section as though they were
measurements.
