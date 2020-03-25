# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3

from ListNode import ListNode
# 1->1->1->2->3->3->4

# In this method, an additional loop is skip through all the duplicates, but is messy with all the checks
def remove_duplicates(head):
    if not head:
        return None
    current = head
    while current is not None and current.next is not None:
        while current.next is not None and current.val != current.next.val:
            current = current.next
        dup = current.next
        while dup is not None and dup.next is not None and dup.val == dup.next.val:
            dup = dup.next
        if dup is not None:
            current.next = dup.next
        current = current.next
    return head

# Much cleaner method. My just repetitively skipping and only moving current when there isn't a duplicate, we can
# perform the same operation using much more concise code
def remove_duplicates_cleaner(head):
    current = head
    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


x = ListNode.array_to_LL([1,2])
print(remove_duplicates_cleaner(x))