#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(
    cd "$(dirname "${BASH_SOURCE[0]}")/.." &&
    pwd
)"

ENTRY_DATE="${1:-$(date +%F)}"

if [[ ! "${ENTRY_DATE}" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo "Usage: $0 [YYYY-MM-DD]" >&2
    exit 1
fi

YEAR="${ENTRY_DATE%%-*}"
ENTRY="${PROJECT_ROOT}/journal/${YEAR}/${ENTRY_DATE}.md"

mkdir -p "$(dirname "${ENTRY}")"

if [[ -e "${ENTRY}" ]]; then
    echo "Journal entry already exists: ${ENTRY}"
    exit 0
fi

cat > "${ENTRY}" <<JOURNAL
# ${ENTRY_DATE}

## Objective

What do I want to accomplish today?

## Work performed

- 

## Commands and configuration

~~~bash
# Relevant commands
~~~

## Observations

- 

## Results

- 

## Problems and anomalies

- 

## Ideas

- 

## Next steps

- 
JOURNAL

echo "Created: ${ENTRY}"
