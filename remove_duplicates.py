from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val})"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        cur = head
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return dummy


def test_solution_1():
    ls = _build_input([1, 2, 3, 3])
    res = Solution().deleteDuplicates(ls)
    _see_output(res)


def test_solution_2():
    ls = _build_input([1, 1, 1, 1, 1])
    res = Solution().deleteDuplicates(ls)
    _see_output(res)


def _build_input(ls: list[int]):
    dummy = ListNode()
    cur = dummy
    for i in ls:
        cur.next = ListNode(val=i)
        cur = cur.next
    return dummy.next


def _see_output(node: ListNode):
    ls = []
    while node.next is not None:
        ls.append(node.val)
        node = node.next
    print(ls)


test_solution_1()
test_solution_2()
