import pytest
import tracemalloc
import sqlite3
from pathfinder.graph import Graph
from pathfinder.label import Label
from pathfinder.label_set import LabelSet
from pathfinder.priority_queue import LabelPriorityQueue

def test_remove_edge_invalid():
    print("[TEST] test_remove_edge_invalid")
    g = Graph()
    g.add_node('X')
    with pytest.raises(ValueError):
        g.remove_edge('X', 'Y')
    print("  [PASS] remove_edge('X','Y') raised ValueError")
    with pytest.raises(ValueError):
        g.remove_edge('Y', 'Z')
    print("  [PASS] remove_edge('Y','Z') raised ValueError")

def test_sqlite_vs_memory_neighbors(tmp_path):
    print("[TEST] test_sqlite_vs_memory_neighbors")
    # Create SQLite-based graph
    db_file = tmp_path / "graph.db"
    conn = sqlite3.connect(str(db_file))
    conn.execute("CREATE TABLE edges(u TEXT, v TEXT, t REAL, c REAL, s REAL)")
    # Insert edges
    edges = [('A','B',1.0,2.0,3.0), ('A','C',2.0,1.0,4.0), ('B','D',0.5,0.5,0.5)]
    conn.executemany("INSERT INTO edges VALUES(?,?,?,?,?)", edges)
    conn.commit()
    conn.close()
    g_sql = Graph(db_path=str(db_file))
    # Build in-memory equivalent
    g_mem = Graph()
    for u, v, t, c, s in edges:
        g_mem.add_edge(u, v, (t, c, s))
    for node in ['A', 'B', 'C', 'D']:
        nbrs_sql = sorted(list(g_sql.neighbors(node)))
        nbrs_mem = sorted(list(g_mem.neighbors(node))) if hasattr(g_mem, '_adj') and node in g_mem._adj else []
        print(f"  Node {node}: sqlite -> {nbrs_sql}, memory -> {nbrs_mem}")
        assert nbrs_sql == nbrs_mem
    print("  [PASS] SQLite and memory neighbor lists match")

def test_epsilon_pruning_limits_frontier():
    print("[TEST] test_epsilon_pruning_limits_frontier")
    eps = 0.1
    ls = LabelSet(epsilon=eps)
    for i in range(20):
        cost = (i * eps/2, i * eps/2, i * eps/2)
        ls.add(Label(cost, node="X"))
    size = len(ls.labels)
    print(f"  Frontier size after epsilon pruning: {size}")
    assert size < 20
    print("  [PASS] Frontier size is bounded by epsilon pruning")

def test_priority_queue_ordering_and_errors():
    print("[TEST] test_priority_queue_ordering_and_errors")
    pq = LabelPriorityQueue()
    l1 = Label((5,1,1),'A')
    l2 = Label((3,2,2),'B')
    pq.push(l1)
    pq.push(l2)
    popped1 = pq.pop()
    print(f"  Popped first: {popped1}")
    assert popped1 == l2
    popped2 = pq.pop()
    print(f"  Popped second: {popped2}")
    assert popped2 == l1
    with pytest.raises(IndexError):
        pq.pop()
    print("  [PASS] pop() on empty queue raised IndexError")
    with pytest.raises(TypeError):
        pq.push("not a label")
    print("  [PASS] push() invalid type raised TypeError")

def test_memory_overhead_for_labels():
    print("[TEST] test_memory_overhead_for_labels")
    tracemalloc.start()
    snapshot1 = tracemalloc.take_snapshot()
    labels = [Label((i,i,i), node=i) for i in range(10000)]
    snapshot2 = tracemalloc.take_snapshot()
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    total_alloc = sum(stat.size_diff for stat in top_stats)
    print(f"  Total memory allocated for 10000 Labels: {total_alloc} bytes")
    assert total_alloc > 0
    print("  [PASS] Memory profiling shows allocation > 0 bytes")
    tracemalloc.stop()
