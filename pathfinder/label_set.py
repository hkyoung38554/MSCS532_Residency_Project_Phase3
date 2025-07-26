from .label import Label

class LabelSet:
    def __init__(self):
        self.labels = []
        self.verbose = False
        self.stats = {
            "total_attempted": 0,
            "kept": 0,
            "pruned": 0
        }

    def add(self, new_label: Label) -> bool:
        self.stats["total_attempted"] += 1

        # Check if any existing label dominates the new one
        for existing in self.labels:
            if existing.dominates(new_label):
                self.stats["pruned"] += 1
                if self.verbose:
                    print(f"Pruned by dominance: {new_label.cost} by {existing.cost}")
                return False

        # Remove labels that are dominated by the new label
        before = len(self.labels)
        self.labels = [lbl for lbl in self.labels if not new_label.dominates(lbl)]
        after = len(self.labels)

        self.labels.append(new_label)
        self.stats["kept"] += 1

        if self.verbose and before != after:
            print(f"Removed {before - after} dominated labels for {new_label.cost}")
        return True

    def __iter__(self):
        return iter(self.labels)

    def __repr__(self):
        return f"LabelSet({[str(lbl) for lbl in self.labels]})"
