#!/bin/bash
# Run the calculator unit tests from any working directory.
set -euo pipefail

cd "$(dirname "$0")"

python3 -m unittest -v test_calculator
