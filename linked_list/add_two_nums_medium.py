# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# (9 -> 8 -> 4 -> 9) + (5 -> 8 -> 7 )
# (4 -> 7 -> 2 -> 0 -> 1)
# (5 -> 8 -> 7 ) + (9 -> 8 -> 4 -> 9)
# (4 -> 7 -> 2 -> 0 -> 1)
from ListNode import ListNode
def add_two_nums(l1, l2):
    carry_over = 0
    p1, p2 = l1, l2
    while p1.next and p2.next:
        p1.val += p2.val + carry_over
        carry_over = 0
        if p1.val >= 10:
            carry_over += 1
            p1.val %= 10
        p1 = p1.next
        p2 = p2.next
    # case 1 len(l1) == len(l2)
    if not p1.next and not p2.next:
        p1.val += p2.val + carry_over
        if p1.val >= 10:
            p1.val %= 10
            p1.next = ListNode(1)
        return l1
    # case 2 len(l1) > len(l2)
    if p1.next and not p2.next:
        p1.val += p2.val + carry_over
        carry_over = 0
        if p1.val >= 10:
            carry_over += 1
            p1.val %= 10
        p1 = p1.next
    # case 3 len(l1) < len(l2)
    if not p1.next and p2.next:
        p1.val += p2.val + carry_over
        carry_over = 0
        if p1.val >= 10:
            carry_over += 1
            p1.val %= 10
        p1.next = p2.next
        p1 = p1.next
    # last part to manage carryover for last digit
    while p1.next:
        p1.val += carry_over
        carry_over = 0
        if p1.val >= 10:
            carry_over += 1
            p1.val %= 10
        p1 = p1.next
    p1.val += carry_over
    if p1.val >= 10:
        p1.val %= 10
        p1.next = ListNode(1)
    return l1


a = ListNode.array_to_LL([4,4,4])
b = ListNode.array_to_LL([3,3,6,9,9,9])
print(add_two_nums(a, b))
