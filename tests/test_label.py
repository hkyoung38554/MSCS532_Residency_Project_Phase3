import pytest
from pathfinder.label import Label


def test_label_init_and_repr():
    lbl = Label((1.0, 2.0, 3.0), 'X')
    print(f"[TEST] test_label_init_and_repr: created label {lbl}")
    assert lbl.node == 'X'
    assert lbl.cost == (1.0, 2.0, 3.0)
    assert 'Label(node=X' in repr(lbl)
    print("[PASS] test_label_init_and_repr")


def test_invalid_cost():
    print("[TEST] test_invalid_cost: initializing Label with invalid cost tuple")
    with pytest.raises(ValueError):
        Label((1.0, 2.0), 'X')
    print("[PASS] test_invalid_cost: ValueError raised as expected")


def test_dominance():
    l1 = Label((1.0, 2.0, 3.0), 'A')
    l2 = Label((2.0, 2.0, 4.0), 'B')
    print(f"[LOG] test_dominance: comparing {l1} and {l2}")
    assert l1.dominates(l2)
    assert not l2.dominates(l1)
    print("[PASS] test_dominance")