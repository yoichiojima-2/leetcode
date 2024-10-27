from leetcode.libs.linked_list import ListNode


def delete_duplicates(head: ListNode) -> ListNode | None:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
