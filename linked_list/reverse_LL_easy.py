# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

from ListNode import ListNode

# Not as concise as next method
def reverse_iterative(head):
    if not head or head.next is None:
        return head
    p = head
    c = head.next
    n = head.next.next
    p.next = None
    while n is not None:
        c.next = p
        p = c
        c = n
        n = n.next
    c.next = p
    return c

def reverse_concise_iterative(head):
    p = None
    c = head
    while c is not None:
        n = c.next
        c.next = p
        p = c
        c = n
    return p

def reverse_recursive(head):
    def recurse(prev, head):
        if head is None:
            return prev
        n = head.next
        head.next = prev
        return recurse(head, n)
    return recurse(None, head)

x = ListNode.array_to_LL([1])
print(reverse_recursive(None))