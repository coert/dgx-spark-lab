#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# shellcheck disable=SC1091
source "${SCRIPT_DIR}/lib/cluster.sh"

require_head

STAMP="$(date '+%Y%m%d-%H%M%S')"
OUT_DIR="${LAB_ROOT}/results/raw/system-${STAMP}"

mkdir -p "${OUT_DIR}"

capture_local() {
  {
    echo '=== hostname ==='
    hostnamectl

    echo
    echo '=== kernel ==='
    uname -a

    echo
    echo '=== addresses ==='
    ip -br addr

    echo
    echo '=== routes ==='
    ip route

    echo
    echo '=== RDMA ==='
    ibdev2netdev || true
    rdma link show || true

    echo
    echo '=== NVIDIA ==='
    nvidia-smi

    echo
    echo '=== Docker ==='
    docker version
    docker info

    echo
    echo '=== Python tooling ==='
    uv --version || true
    python3 --version || true
  } > "${OUT_DIR}/${HEAD_HOST}.txt" 2>&1
}

capture_worker() {
  run_worker bash -s > "${OUT_DIR}/${WORKER_HOST}.txt" 2>&1 <<'REMOTE'
set -u

echo '=== hostname ==='
hostnamectl

echo
echo '=== kernel ==='
uname -a

echo
echo '=== addresses ==='
ip -br addr

echo
echo '=== routes ==='
ip route

echo
echo '=== RDMA ==='
ibdev2netdev || true
rdma link show || true

echo
echo '=== NVIDIA ==='
nvidia-smi

echo
echo '=== Docker ==='
docker version
docker info

echo
echo '=== Python tooling ==='
uv --version || true
python3 --version || true
REMOTE
}

capture_local
capture_worker

echo "System information written to:"
echo "  ${OUT_DIR}"
