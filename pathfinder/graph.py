class Graph:
    def __init__(self):
        self._adj = {}

    def add_edge(self, src, dst, cost_vector):
        if not isinstance(cost_vector, tuple):
            raise TypeError("Edge cost must be a tuple")
        if src not in self._adj:
            self._adj[src] = []
        if dst not in self._adj:
            self._adj[dst] = []
        self._adj[src].append((dst, cost_vector))

    def neighbors(self, node):
        return list(self._adj.get(node, []))  # Return a copy

    def __contains__(self, node):
        return node in self._adj

    def __repr__(self):
        return f"Graph({len(self._adj)} nodes)"
