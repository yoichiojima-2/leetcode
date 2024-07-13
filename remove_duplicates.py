from typing import Optional
import pdb


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
            # pdb.set_trace()
        return dummy


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        temp = head
        temp2 = head.next
        last = head.val

        while temp2:  # while end of Linked list
            if temp2.val == last:  # Current number same as last number
                if not temp2.next:  # If last element, just delete and break loop
                    pdb.set_trace()
                    temp.next = None
                    break
                temp2 = temp2.next  # Not last, then delete that element
                temp.next = temp2  # and move to next element
            else:  # If not the same as last element, jump to next node
                temp = temp2
                last = temp.val
                temp2 = temp2.next

        return head  # return the head back


def test_solution_1():
    ls = _build_input([1, 2, 3, 3])
    res = Solution().deleteDuplicates(ls)
    assert to_list(res) == [1, 2, 3]


def test_solution_2():
    ls = _build_input([1, 1, 1, 1, 1])
    res = Solution().deleteDuplicates(ls)
    assert to_list(res) == [1]


def _build_input(ls: list[int]):
    dummy = ListNode()
    cur = dummy
    for i in ls:
        cur.next = ListNode(val=i)
        cur = cur.next
    return dummy.next


def to_list(node: ListNode):
    ls = []
    while node is not None:
        ls.append(node.val)
        node = node.next
    return ls


test_solution_1()
test_solution_2()
