#!/usr/bin/env bash
echo "Running all tests..."
pytest --maxfail=1 --disable-warnings -q > test_results.txt
echo "Results written to test_results.txt"
