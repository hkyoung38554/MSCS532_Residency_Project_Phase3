from functools import lru_cache
from typing import Any, Tuple, Optional

class Label:
    """
    Lightweight label object with __slots__ to reduce memory overhead,
    and memoized dominance checks for performance.
    """
    __slots__ = ("cost", "node", "predecessor")

    def __init__(self,
                 cost: Tuple[float, float, float],
                 node: Any,
                 predecessor: Optional['Label'] = None):
        if not (isinstance(cost, tuple) and len(cost) == 3):
            raise ValueError("Cost must be a tuple of three floats")
        self.cost = cost
        self.node = node
        self.predecessor = predecessor

    @staticmethod
    @lru_cache(maxsize=10_000)
    def _dominance_key(a: Tuple[float, float, float],
                       b: Tuple[float, float, float]) -> bool:
        """True if a ≤ b in all dims and < in at least one."""
        return (all(x <= y for x, y in zip(a, b))
                and any(x < y for x, y in zip(a, b)))

    def dominates(self, other: 'Label') -> bool:
        """Memoized Pareto dominance check."""
        return Label._dominance_key(self.cost, other.cost)

    def __lt__(self, other: 'Label') -> bool:
        """Lexicographic for (time, toll, scenic)."""
        return self.cost < other.cost

    def __repr__(self) -> str:
        return f"Label(node={self.node}, cost={self.cost})"
