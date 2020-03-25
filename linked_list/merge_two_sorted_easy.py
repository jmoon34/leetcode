# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing
# together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

from ListNode import ListNode

# this method preserves l1 and l2, but realized that that's unnecessary
# also because it starts at one of the heads, handling the edge cases are annoying
# much better to start from an empty node and return .next as shown in the second method
def merge_two_lists(l1, l2):
    if l1 is None and l2 is None:
        return None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    p1, p2 = l1, l2
    if l1.val <= l2.val:
        l3 = l1
        p1 = p1.next
    else:
        l3 = l2
        p2 = p2.next
    p3 = l3
    while p1 is not None and p2 is not None:
        if p1.val > p2.val:
            p3.next = p2
            p2 = p2.next
            p3 = p3.next
        else:
            p3.next = p1
            p1 = p1.next
            p3 = p3.next
    if p1 is None:
        p3.next = p2
    if p2 is None:
        p3.next = p1
    return l3

def merge_two_lists_better(l1, l2):
    l3 = ListNode()
    p3 = l3
    while l1 and l2:
        if l1.val <= l2.val:
            p3.next = l1
            l1 = l1.next
        else:
            p3.next = l2
            l2 = l2.next
        p3 = p3.next
    if l1:
        p3.next = l1
    if l2:
        p3.next = l2
    return l3.next