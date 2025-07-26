import pytest
from pathfinder.priority_queue import LabelPriorityQueue
from pathfinder.label import Label


def test_push_and_pop():
    pq = LabelPriorityQueue()
    l1 = Label((5.0, 1.0, 1.0), 'A')
    l2 = Label((3.0, 2.0, 2.0), 'B')
    print(f"[TEST] test_push_and_pop: pushing labels {l1}, {l2}")
    pq.push(l1)
    pq.push(l2)
    print(f"[LOG] Queue content before pop: {pq}")
    popped = pq.pop()
    print(f"[LOG] Popped label: {popped}")
    assert popped == l2  # lexicographically smaller
    print("[PASS] test_push_and_pop")


def test_empty_pop():
    pq = LabelPriorityQueue()
    print("[TEST] test_empty_pop: popping from empty queue")
    with pytest.raises(IndexError):
        pq.pop()
    print("[PASS] test_empty_pop")


def test_push_type_error():
    pq = LabelPriorityQueue()
    print("[TEST] test_push_type_error: pushing invalid type")
    with pytest.raises(TypeError):
        pq.push("not a label")
    print("[PASS] test_push_type_error")