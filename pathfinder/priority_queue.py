import heapq
from typing import List
from .label import Label

class LabelPriorityQueue:
    """
    Min‑heap over Label using lexicographic cost ordering.
    """
    __slots__ = ("_heap",)

    def __init__(self):
        self._heap: List[Label] = []

    def push(self, label: Label) -> None:
        if not isinstance(label, Label):
            raise TypeError("Can only push Label instances")
        heapq.heappush(self._heap, label)

    def pop(self) -> Label:
        if not self._heap:
            raise IndexError("Pop from empty priority queue")
        return heapq.heappop(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)

    def __len__(self) -> int:
        return len(self._heap)

    def __repr__(self) -> str:
        return f"LabelPriorityQueue({self._heap})"