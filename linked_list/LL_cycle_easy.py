# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
# the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
# Follow up:
# Can you solve it using O(1) (i.e. constant) memory?

from ListNode import ListNode

# initially wrote a method that returns the index of where the cycle begins
# O(n) time and O(n) space since it uses a hash table
def cycle_with_memory(head):
    d = {}
    current = head
    index = 0
    while current and current not in d:
        d[current] = index
        current = current.next
        index += 1
    return current is not None
    # if not current:
    #     return False
    # return d[current]

# O(n) time and O(1) space but this alters the content of the LL, so don't think it's a good method
# works by changing all visited node's val to None
def cycle_destructive(head):
    current = head
    while current and current.val:
        current.val = None
        current = current.next
    # if no cycle, current should be None
    if not current:
        return False
    # if there is a cycle, current should be at the start of the cycle with current.val = None
    if not current.val:
        return True

def cycle_two_pointer(head):
    if not head or not head.next:
        return False
    slow, fast = head, head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

x = ListNode.array_to_LL([1,2,3,4])
# tail = x.next.next.next
# tail.next = x.next.next
print(cycle_slow(x))
