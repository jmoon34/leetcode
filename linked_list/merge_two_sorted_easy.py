# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing
# together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

from ListNode import ListNode

# this method preserves l1 and l2
def merge_two_lists(l1, l2):
    c1, c2 = l1, l2
    l3 = ListNode(0)
    c3 = l3
    while c1 and c2:
        if c1.val <= c2.val:
            c3.next = c1
            c1 = c1.next
        else:
            c3.next = c2
            c2 = c2.next
        c3 = c3.next
    c3.next = c1 or c2

    return l3.next

def merge_two_lists_mutate(l1, l2):
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

def merge_two_lists_rec(l1, l2):
    l3 = ListNode(0)
    n3 = l3
    def recurse(n1, n2, n3):
        if not n1 and not n2:
            return
        elif not n1:
            n3.next = n2
            return
        elif not n2:
            n3.next = n1
            return
        if n1.val <= n2.val:
            n3.next = n1
            recurse(n1.next, n2, n3.next)
        else:
            n3.next = n2
            recurse(n1, n2.next, n3.next)

    recurse(l1, l2, n3)
    return l3.next