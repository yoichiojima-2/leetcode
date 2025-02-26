from leetcode.has_cycle import Solution, ListNode


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
    assert Solution().hasCycle(head) == False
