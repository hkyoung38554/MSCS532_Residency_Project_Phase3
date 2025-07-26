import pytest
from pathfinder.label_set import LabelSet
from pathfinder.label import Label


def test_labelset_add_and_prune():
    ls = LabelSet()
    print(f"[TEST] test_labelset_add_and_prune: initial labels {ls.labels}")
    assert ls.add(Label((1.0, 1.0, 1.0), 'X'))
    print(f"[LOG] After adding (1.0,1.0,1.0): {ls.labels}")
    # dominated by existing
    assert not ls.add(Label((2.0, 2.0, 2.0), 'X'))
    print(f"[LOG] After attempting dominated add (2.0,2.0,2.0): {ls.labels}")
    # non-dominated different tradeoff
    assert ls.add(Label((1.5, 0.5, 1.0), 'X'))
    print(f"[LOG] After adding non-dominated (1.5,0.5,1.0): {ls.labels}")
    assert len(ls.labels) == 2
    print("[PASS] test_labelset_add_and_prune")


def test_type_error():
    ls = LabelSet()
    print("[TEST] test_type_error: adding invalid type")
    with pytest.raises(TypeError):
        ls.add("not a label")
    print("[PASS] test_type_error")