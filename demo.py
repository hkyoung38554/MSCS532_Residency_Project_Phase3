import time
from contextlib import redirect_stdout
from pathfinder.graph import Graph
from pathfinder.label import Label
from pathfinder.label_set import LabelSet
from pathfinder.priority_queue import LabelPriorityQueue

def generate_large_graph(n):
    """Generates a synthetic directed graph with n nodes and 3D cost edges."""
    g = Graph()
    for i in range(n - 1):
        g.add_edge(f"N{i}", f"N{i+1}", (i % 5 + 1, (i * 2) % 7 + 1, (i * 3) % 11 + 1))
    return g

def optimized_pareto_pathfinding(graph, source):
    label_sets = {node: LabelSet() for node in graph._adj}
    pq = LabelPriorityQueue()
    start = Label((0, 0, 0), source)
    label_sets[source].add(start)
    pq.push(start)

    expansions = 0
    while pq:
        lbl = pq.pop()
        expansions += 1
        for nbr, cost in graph.neighbors(lbl.node):
            new_cost = tuple(x + y for x, y in zip(lbl.cost, cost))
            new_lbl = Label(new_cost, nbr, lbl)
            if label_sets[nbr].add(new_lbl):
                pq.push(new_lbl)
    return label_sets, expansions

if __name__ == '__main__':
    with open('demo_results.txt', 'w') as f:
        with redirect_stdout(f):
            print("=== Phase 3 Optimized Demo ===")
            start_time = time.time()
            g = generate_large_graph(100)
            labels, expansions = optimized_pareto_pathfinding(g, 'N0')
            elapsed = time.time() - start_time
            print(f"Nodes expanded: {expansions}")
            print(f"Execution time: {elapsed:.4f} seconds")
            for node in sorted(labels.keys()):
                if labels[node].labels:
                    print(f"{node}: {[l.cost for l in labels[node].labels]}")
