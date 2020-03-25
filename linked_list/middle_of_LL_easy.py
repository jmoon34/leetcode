# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
#
# If there are two middle nodes, return the second middle node.
#
#
#
# Example 1:
#
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:
#
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.
#
#
# Note:
#
# The number of nodes in the given list will be between 1 and 100.

# [1,2,3,4,5,6,7] odd case
# 11, 32, 53, 74, if next is None return p2
# [1,2,3,4,5,6] even case
# 11, 32, 53,None4
from ListNode import ListNode

def middle_node(head):
    if not head:
        return None
    mid = head
    while head is not None and head.next is not None:
        print(mid, head)
        head = head.next.next
        mid = mid.next
    return mid

h = ListNode.array_to_LL([1,2,3,4,5,6])
print([h])
