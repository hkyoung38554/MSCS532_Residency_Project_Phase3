import sqlite3
from typing import Any, Dict, Tuple, List, Iterator

class Graph:
    """
    Scalable graph supporting on‑disk storage for large datasets.
    If `db_path` is None, falls back to in‑memory dict adjacencies.
    """

    def __init__(self, db_path: str = None):
        if db_path:
            # Store edges in SQLite: table edges(u TEXT, v TEXT, t REAL, c REAL, s REAL)
            self._conn = sqlite3.connect(db_path)
            self._in_memory = False
        else:
            # Fallback to dict-of-dicts adjacency
            self._adj: Dict[Any, Dict[Any, Tuple[float, float, float]]] = {}
            self._in_memory = True

    def add_node(self, node: Any) -> None:
        if self._in_memory:
            self._adj.setdefault(node, {})

    def add_edge(self, u: Any, v: Any, cost: Tuple[float, float, float]) -> None:
        if not (isinstance(cost, tuple) and len(cost) == 3):
            raise ValueError("Cost must be a tuple of three floats")
        if self._in_memory:
            self.add_node(u); self.add_node(v)
            self._adj[u][v] = cost
        else:
            t, c, s = cost
            self._conn.execute(
                "INSERT INTO edges(u, v, t, c, s) VALUES (?, ?, ?, ?, ?)",
                (u, v, t, c, s)
            )
            self._conn.commit()

    def remove_edge(self, u: Any, v: Any) -> None:
        if self._in_memory:
            try:
                del self._adj[u][v]
            except KeyError:
                raise ValueError(f"Edge {u} -> {v} not found")
        else:
            cur = self._conn.execute(
                "DELETE FROM edges WHERE u = ? AND v = ?", (u, v)
            )
            if cur.rowcount == 0:
                raise ValueError(f"Edge {u} -> {v} not found")
            self._conn.commit()

    def neighbors(self, node: Any) -> Iterator[Tuple[Any, Tuple[float, float, float]]]:
        if self._in_memory:
            if node not in self._adj:
                raise KeyError(f"Node {node} not found")
            yield from self._adj[node].items()
        else:
            cur = self._conn.execute(
                "SELECT v, t, c, s FROM edges WHERE u = ?", (node,)
            )
            for v, t, c, s in cur:
                yield v, (t, c, s)

    def bfs(self, start: Any) -> List[Any]:
        from collections import deque
        if self._in_memory and start not in self._adj:
            raise KeyError(f"Node {start} not found")
        visited, order = {start}, []
        q = deque([start])
        while q:
            u = q.popleft()
            order.append(u)
            for v, _ in self.neighbors(u):
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return order

    def dfs(self, start: Any) -> List[Any]:
        if self._in_memory and start not in self._adj:
            raise KeyError(f"Node {start} not found")
        visited, order = set(), []
        def _rec(u):
            visited.add(u)
            order.append(u)
            for v, _ in self.neighbors(u):
                if v not in visited:
                    _rec(v)
        _rec(start)
        return order
