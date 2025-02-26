class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        seen = set()
        while head is not None:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


def test_has_cycle():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # Create a cycle
    assert Solution().hasCycle(head) == True


def test_no_cycle():
    head = ListNode(1)
    head.next = ListNode(2)