#!/bin/bash -xe

SCENARIOS=${1:-default}
PYTHONS=${2:-python3.6 python3.7 python3.8}

for scenario in ${SCENARIOS}; do
  for venv in ${PYTHONS}; do
    molecule test -s ${scenario}-${venv}
  done
done
