# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

from ListNode import ListNode

# p->6->6->2->3->6->3->6
def remove_element_iterative(head, val):
    p = ListNode()
    p.next = head
    current = p
    while current:
        while current.next and current.next.val == val:
            current.next = current.next.next
        current = current.next
    return p.next

x = ListNode.array_to_LL([1,6,6,2,3,6,3,6])
print(remove_element_iterative(x, 3))