from typing import List
from .label import Label

class LabelSet:
    """
    Pareto‑front manager with ε‑pruning to control frontier size.
    """
    __slots__ = ("labels", "epsilon")

    def __init__(self, epsilon: float = 0.0):
        self.labels: List[Label] = []
        self.epsilon = epsilon

    def add(self, label: Label) -> bool:
        """
        Insert label if not ε‑dominated; prune ε‑dominated existing ones.
        Returns True if added.
        """
        if not isinstance(label, Label):
            raise TypeError("Can only add Label instances")
        new = []
        eps = self.epsilon
        for existing in self.labels:
            # existing ε‑dominates label?
            if all(e <= l + eps for e, l in zip(existing.cost, label.cost)):
                return False
            # keep existing if not ε‑dominated by label
            if not all(l <= e + eps for l, e in zip(label.cost, existing.cost)):
                new.append(existing)
        new.append(label)
        self.labels = new
        return True

    def __repr__(self) -> str:
        return f"LabelSet(epsilon={self.epsilon}, labels={self.labels})"
