#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# shellcheck disable=SC1091
source "${SCRIPT_DIR}/lib/cluster.sh"

require_head
require_command ssh
require_command ip
require_command nc

echo "=== Nodes ==="
printf '%-18s %s\n' "Head:" "${HEAD_HOST} (${HEAD_IP})"
printf '%-18s %s\n' "Worker:" "${WORKER_HOST} (${WORKER_IP})"

echo
echo "=== SSH ==="
run_worker hostname

echo
echo "=== Rail 0 ==="
ip -br addr show "${ETH_IF_0}"
run_worker "ip -br addr show '${ETH_IF_0}'"
ping -c 2 -I "${ETH_IF_0}" "${WORKER_IP}"

echo
echo "=== Rail 1 ==="
ip -br addr show "${ETH_IF_1}"
run_worker "ip -br addr show '${ETH_IF_1}'"
ping -c 2 -I "${ETH_IF_1}" 10.201.0.2

echo
echo "=== RDMA ==="
ibdev2netdev
run_worker ibdev2netdev

echo
echo "=== GPUs ==="
nvidia-smi --query-gpu=name,driver_version --format=csv,noheader
run_worker \
  "nvidia-smi --query-gpu=name,driver_version --format=csv,noheader"

echo
echo "=== Docker image ==="
docker image inspect "${VLLM_IMAGE}" \
  --format 'head:   {{.Id}}'

run_worker \
  "docker image inspect '${VLLM_IMAGE}' \
   --format 'worker: {{.Id}}'"

echo
echo "Cluster health check completed."
