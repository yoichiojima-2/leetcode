import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from remove_duplicates import ListNode, delete_duplicates


def test_1():
    input_ = ListNode.new([1, 1, 2])
    print("input:", list(input_.collect()))
    res = delete_duplicates(input_)
    print("output:", list(res.collect()))
    assert list(res.collect()) == [1, 2]


def test_2():
    input_ = ListNode.new([1, 1, 2, 3, 3])
    print("input:", list(input_.collect()))
    res = delete_duplicates(input_)
    print("output:", list(res.collect()))
    assert list(res.collect()) == [1, 2, 3]
