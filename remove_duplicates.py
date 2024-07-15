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
        head = self
        while head is not None:
            yield head.val
            head = head.next


def delete_duplicates(head: ListNode) -> ListNode | None:
    cur = head
    while cur.next.next is not None:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        cur = cur.next
    return head
        



def test_1():
    ls = ListNode.new([1, 1, 2])
    res = list(ls.collect())
    assert res == [1, 2]

def test_2():
    ls = ListNode.new([1, 1, 2, 3, 3])
    res = list(ls.collect())
    assert res == [1, 2, 3]
