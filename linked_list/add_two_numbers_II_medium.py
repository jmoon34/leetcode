# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


from ListNode import ListNode

# construct the two integers from the linked list
def add_two_numbers_integer(l1, l2):
    n1, n2 = l1.val, l2.val
    p1, p2 = l1.next, l2.next
    while p1:
        n1 = (n1*10 + p1.val)
        p1 = p1.next
    while p2:
        n2 = (n2*10 + p2.val)
        p2 = p2.next
    s = str(n1 + n2)
    print(s)
    result = ListNode(0)
    pr = result
    for digit in s:
        pr.next = ListNode(int(digit))
        pr = pr.next
    return result.next




x = ListNode.array_to_LL([7,2,4,3])
y = ListNode.array_to_LL([5,6,4])
print(add_two_numbers_integer(x, y))