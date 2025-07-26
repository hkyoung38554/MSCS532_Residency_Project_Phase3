# MSCS532 Residency Project Phase 3: Optimized Multi-Criteria Pathfinder

This repository contains the Phase 3 implementation of the Multi-Criteria Pathfinder project for MSCS532. The objective of this phase is to optimize the performance and scalability of the original Pareto-based pathfinding system developed in Phase 2.

## Overview

The pathfinding system computes Pareto-optimal paths in a directed graph with multi-dimensional cost vectors. Each path is evaluated based on multiple criteria (e.g., time, cost, risk), and only non-dominated solutions are preserved.

This phase focuses on:
- Performance optimization through label pruning and memory-efficient structures
- Scalability improvements for large graphs (100+ nodes)
- Runtime analysis and stress testing
- Clean modular design ready for further enhancements

## Key Features

- Efficient LabelSet filtering using dominance logic
- Priority queue with custom label comparison
- Synthetic graph generation for stress testing
- Performance logging (timing, label expansion count)
- Updated testable demo in `demo.py`

## Directory Structure

```
.
├── demo.py
├── demo_results.txt
├── pathfinder
│   ├── __init__.py
│   ├── graph.py
│   ├── label.py
│   ├── label_set.py
│   └── priority_queue.py
├── scripts
│   └── run_tests.sh
├── tests
│   ├── __init__.py
│   ├── test_graph.py
│   ├── test_label.py
│   ├── test_label_set.py
│   ├── test_priority_queue.py
│   └── test_results.txt
├── requirements.txt
├── README.md
└── Project Phase 3 Deliverable 3 Report.pdf
```

## How to Run

To test the optimized pathfinding logic:

```bash
python demo.py
```

Results, including execution time and label statistics, will be saved to `demo_results.txt`.

To run all tests:
```bash
bash scripts/run_tests.sh
```

## Requirements

Python 3.7+

Install dependencies (if any):

```bash
pip install -r requirements.txt
```

> Note: The implementation uses only standard Python libraries.

## Optimization Highlights

- LabelSet tracks label pruning effectiveness
- PriorityQueue logs heap activity for performance insights
- demo.py now generates large graphs and profiles search runtime

## Phase 3 Deliverables

- Optimized source code reflecting report strategies
- GitHub repository containing final implementation
- Phase 3 evaluation report (submitted separately)

## Author

Haeri Kyoung  
MSCS532 – University of the Cumberlands  
Alternative Investments Team – Apex Fintech Solutions
