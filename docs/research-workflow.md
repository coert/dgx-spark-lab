# Research Workflow

Every substantial topic should progress through four stages.

## 1. Theory

Document the problem, terminology, algorithms, mathematical model, and expected
trade-offs.

## 2. Architecture

Describe how the mechanism is used in real systems. Include communication
patterns, placement, memory ownership, and failure modes.

## 3. Implementation

Build the smallest correct prototype first. Move to production frameworks only
after the essential mechanism is understood.

## 4. Benchmark

Measure:

- correctness
- latency
- throughput
- GPU utilization
- CPU utilization
- memory use
- network traffic
- scaling efficiency

Every topic should conclude with:

- what was learned
- what remains uncertain
- a concrete follow-up challenge
