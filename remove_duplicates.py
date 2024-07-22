from __future__ import annotations
from typing import Iterable


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def new(ls):
        head = ListNode()
        cur = head
        for i in ls:
            cur.next = ListNode(val=i)
            cur = cur.next
        return head.next

    def collect(self) -> Iterable[int]:
        if self.next is None:
            return [self.val]
        head = self
        while head is not None:
            yield head.val
            head = head.next


def delete_duplicates(head: ListNode) -> ListNode | None:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


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
