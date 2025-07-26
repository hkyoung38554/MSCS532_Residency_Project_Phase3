# Multi-Criteria Pathfinding Engine – Phase 3

This project demonstrates a scalable, optimized implementation of a Pareto-optimal pathfinding algorithm using multi-criteria shortest paths.

## Overview

The system expands on the Phase 2 proof-of-concept and introduces key improvements in algorithmic efficiency, scalability, and robustness. It operates on graphs where each edge has multi-dimensional cost vectors (e.g., time, distance, cost), and computes Pareto-optimal paths between nodes.

## Directory Structure

```
Project Phase 3 Deliverable 3/
├── pathfinder/
│   ├── __init__.py
│   ├── graph.py
│   ├── label.py
│   ├── label_set.py
│   └── priority_queue.py
├── tests/
│   ├── performance_tests.py
│   ├── test_validation.py
│   ├── performance_results.txt
│   └── validation_results.txt
├── requirements.txt
├── README.md
└── Project Phase 3 Deliverable 3 Report.pdf
```

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run performance and validation tests:
```
python tests/performance_tests.py
python tests/test_validation.py
```

## Features

- Supports multi-dimensional edge costs
- Pareto-optimal label dominance checking
- Scales to large graphs (tested up to 2000 nodes / 10,000 edges)
- Validation and performance logging

## Notes

- Optimization strategies and evaluation results are documented in the project report.
- Refer to `performance_results.txt` and `validation_results.txt` for benchmark data.