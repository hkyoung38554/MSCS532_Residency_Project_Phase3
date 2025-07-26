class Label:
    def __init__(self, cost, node, prev=None):
        if not isinstance(cost, tuple):
            raise TypeError("Cost must be a tuple")
        if len(cost) < 2:
            raise ValueError("Cost vector must have at least 2 dimensions")
        self.cost = cost
        self.node = node
        self.prev = prev  # reference to previous Label

    def dominates(self, other):
        """Returns True if self dominates other in all cost dimensions"""
        less_equal = all(s <= o for s, o in zip(self.cost, other.cost))
        strictly_less = any(s < o for s, o in zip(self.cost, other.cost))
        return less_equal and strictly_less

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost and self.node == other.node

    def __hash__(self):
        return hash((self.cost, self.node))

    def __repr__(self):
        return f"<{self.node}: {self.cost}>"
