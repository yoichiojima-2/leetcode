import pytest

from leetcode.libs.linked_list import ListNode
from leetcode.remove_duplicates import delete_duplicates


@pytest.fixture
def linked_list_1() -> ListNode:
    return ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2)))


@pytest.fixture
def linked_list_2() -> ListNode:
    return ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))


def test_1(linked_list_1: ListNode):
    res = delete_duplicates(linked_list_1)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next is None


def test_2(linked_list_2: ListNode):
    res = delete_duplicates(linked_list_2)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 3
    assert res.next.next.next is None
