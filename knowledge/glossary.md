# Glossary

## AllGather

A collective operation in which every participant receives the data contributed
by every other participant.

## AllReduce

A collective operation that combines values from every participant and returns
the reduced result to every participant.

## DDP

Distributed Data Parallel. Each worker holds a complete model replica and
processes a different data batch. Gradients are synchronized between workers.

## FSDP

Fully Sharded Data Parallel. Parameters, gradients, and optimizer state can be
sharded across workers.

## GPUDirect RDMA

A mechanism that permits supported network adapters to transfer data directly
to and from GPU-accessible memory without staging it through ordinary host
buffers.

## NCCL

NVIDIA Collective Communications Library. Provides optimized GPU collectives
such as AllReduce, AllGather, ReduceScatter, and Broadcast.

## Pipeline Parallelism

A model is divided into sequential stages placed on different devices.

## ReduceScatter

A collective that reduces data across participants and distributes a different
portion of the result to each participant.

## Tensor Parallelism

Individual tensor operations are partitioned across multiple devices.
