import heapq
from .label import Label

class LabelPriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0
        self.verbose = False
        self.stats = {
            "pushed": 0,
            "popped": 0
        }

    def push(self, label: Label):
        heapq.heappush(self.heap, (label.cost, self.count, label))
        self.count += 1
        self.stats["pushed"] += 1
        if self.verbose:
            print(f"Pushed: {label.node} {label.cost}")

    def pop(self) -> Label:
        _, _, label = heapq.heappop(self.heap)
        self.stats["popped"] += 1
        if self.verbose:
            print(f"Popped: {label.node} {label.cost}")
        return label

    def __bool__(self):
        return bool(self.heap)

    def __len__(self):
        return len(self.heap)
