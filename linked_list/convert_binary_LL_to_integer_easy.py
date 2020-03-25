# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either
# 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
#
# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2:
# Input: head = [0]
# Output: 0

# Example 3:
# Input: head = [1]
# Output: 1

# Example 4:
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880

# Example 5:
# Input: head = [0,0]
# Output: 0
#
# Constraints:
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.

from ListNode import ListNode

def bin_LL_to_dec(head):
    exp = 0
    d = []
    current = head
    while current:
        d.append([current.val, exp])
        exp += 1
        current = current.next
    max_exp = exp-1
    print(max_exp)
    for digit in d:
        digit[1] = max_exp - digit[1]
    return sum([digit*2**exp for digit, exp in d])

x = ListNode.array_to_LL([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
print(bin_LL_to_dec(x))