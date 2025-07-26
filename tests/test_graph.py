import pytest
from pathfinder.graph import Graph

@pytest.fixture
def simple_graph():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_edge('A', 'B', (1.0, 2.0, 3.0))
    print(f"[LOG] Created simple_graph with adjacency: {g._adj}")
    return g


def test_add_node(simple_graph):
    print("[TEST] test_add_node: verifying nodes A and B exist")
    assert 'A' in simple_graph._adj
    assert 'B' in simple_graph._adj
    print(f"[PASS] test_add_node: nodes found: {list(simple_graph._adj.keys())}")


def test_remove_node(simple_graph):
    print("[TEST] test_remove_node: removing node 'B'")
    simple_graph.remove_node('B')
    print(f"[LOG] After removal, adjacency: {simple_graph._adj}")
    assert 'B' not in simple_graph._adj
    print("[TEST] test_remove_node: verifying removal of non-existent node 'Z' raises KeyError")
    with pytest.raises(KeyError):
        simple_graph.remove_node('Z')
    print("[PASS] test_remove_node: KeyError raised for 'Z'")


def test_add_remove_edge(simple_graph):
    print("[TEST] test_add_remove_edge: removing edge A->B")
    simple_graph.remove_edge('A', 'B')
    print(f"[LOG] After edge removal, adjacency A: {simple_graph._adj.get('A')}")
    with pytest.raises(ValueError):
        print("[TEST] test_add_remove_edge: verifying removing same edge again raises ValueError")
        simple_graph.remove_edge('A', 'B')
    print("[PASS] test_add_remove_edge: ValueError raised for missing edge")


def test_neighbors(simple_graph):
    print("[TEST] test_neighbors: retrieving neighbors of 'A'")
    neighbors = simple_graph.neighbors('A')
    print(f"[LOG] Neighbors of A: {neighbors}")
    assert neighbors == [('B', (1.0, 2.0, 3.0))]
    print("[TEST] test_neighbors: verifying retrieving neighbors of non-existent node 'Z' raises KeyError")
    with pytest.raises(KeyError):
        simple_graph.neighbors('Z')
    print("[PASS] test_neighbors: KeyError raised for 'Z'")


def test_bfs_dfs(simple_graph):
    print("[TEST] test_bfs_dfs: adding edge B->C and testing traversals")
    g = simple_graph
    g.add_edge('B', 'C', (0.0, 0.0, 0.0))
    bfs_order = g.bfs('A')
    dfs_order = g.dfs('A')
    print(f"[LOG] BFS order: {bfs_order}")
    print(f"[LOG] DFS order: {dfs_order}")
    assert bfs_order == ['A', 'B', 'C']
    assert dfs_order == ['A', 'B', 'C']
    print("[PASS] test_bfs_dfs: BFS and DFS orders correct")