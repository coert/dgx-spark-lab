#!/usr/bin/env bash

set -euo pipefail

LAB_ROOT="$(
  cd "$(dirname "${BASH_SOURCE[0]}")/../.." &&
  pwd
)"

# shellcheck disable=SC1091
source "${LAB_ROOT}/config/cluster.env"

if [[ -f "${LAB_ROOT}/config/secrets.env" ]]; then
  # shellcheck disable=SC1091
  source "${LAB_ROOT}/config/secrets.env"
fi

log() {
  printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*"
}

die() {
  printf 'Error: %s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 ||
    die "Required command not found: $1"
}

run_worker() {
  ssh \
    -o BatchMode=yes \
    -o ConnectTimeout=5 \
    "${WORKER_IP}" \
    "$@"
}

host_name() {
  hostname --short
}

is_head() {
  [[ "$(host_name)" == "${HEAD_HOST}" ]]
}

require_head() {
  is_head || die "Run this command on ${HEAD_HOST}"
}
