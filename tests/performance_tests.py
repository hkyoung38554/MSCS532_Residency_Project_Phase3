import time
import random
from pathfinder.graph import Graph
from pathfinder.label import Label
from pathfinder.label_set import LabelSet
from pathfinder.priority_queue import LabelPriorityQueue

def benchmark_graph_operations(num_nodes, avg_degree):
    # Create random graph
    g = Graph()
    nodes = list(range(num_nodes))
    for u in nodes:
        g.add_node(u)
    # Generate edges
    edges = []
    for u in nodes:
        for _ in range(avg_degree):
            v = random.choice(nodes)
            cost = (random.random(), random.random(), random.random())
            edges.append((u, v, cost))
    # Benchmark add_edge
    start = time.time()
    for u, v, cost in edges:
        g.add_edge(u, v, cost)
    t_add = time.time() - start
    # Benchmark neighbors lookup
    start = time.time()
    for u in random.sample(nodes, min(1000, num_nodes)):
        _ = list(g.neighbors(u))
    t_neighbors = time.time() - start
    # Benchmark remove_edge
    start = time.time()
    for u, v, _ in random.sample(edges, min(1000, len(edges))):
        try:
            g.remove_edge(u, v)
        except ValueError:
            pass
    t_remove = time.time() - start

    return t_add, t_neighbors, t_remove

def benchmark_labelset_operations(size_frontier, num_tests):
    # Create random labels
    ls = LabelSet(epsilon=0.0)
    labels = []
    for _ in range(size_frontier):
        cost = (random.random(), random.random(), random.random())
        labels.append(Label(cost, node="X"))
    # Add to frontier
    for lbl in labels:
        ls.add(lbl)
    # Benchmark insertion of random labels
    test_labels = [Label((random.random(), random.random(), random.random()), node="X") for _ in range(num_tests)]
    start = time.time()
    for lbl in test_labels:
        ls.add(lbl)
    t_insert = time.time() - start
    return t_insert

def benchmark_pq_operations(num_items):
    pq = LabelPriorityQueue()
    items = [Label((random.random(), random.random(), random.random()), node=i) for i in range(num_items)]
    # Benchmark push
    start = time.time()
    for lbl in items:
        pq.push(lbl)
    t_push = time.time() - start
    # Benchmark pop
    start = time.time()
    while pq:
        pq.pop()
    t_pop = time.time() - start
    return t_push, t_pop

def run_all_benchmarks():
    print("Graph Benchmark (nodes, degree):")
    for n in [1000, 5000, 10000]:
        t_add, t_neighbors, t_remove = benchmark_graph_operations(n, avg_degree=10)
        print(f"  N={n}, add: {t_add:.4f}s, neighbors(1000): {t_neighbors:.4f}s, remove(1000): {t_remove:.4f}s")
    print("\nLabelSet Benchmark (frontier size):")
    for m in [1000, 5000, 10000]:
        t_insert = benchmark_labelset_operations(m, num_tests=1000)
        print(f"  M={m}, insert 1000 labels: {t_insert:.4f}s")
    print("\nPriorityQueue Benchmark (items):")
    for k in [1000, 5000, 10000]:
        t_push, t_pop = benchmark_pq_operations(k)
        print(f"  K={k}, push {k}: {t_push:.4f}s, pop {k}: {t_pop:.4f}s")

if __name__ == "__main__":
    run_all_benchmarks()
