# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
#
# Example 2:
# Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
#
# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.


def intersection_dict(headA, headB):
    d = {}
    p_1, p_2 = headA, headB
    index = 0
    while p_1:
        d[p_1] = index
        index += 1
        p_1 = p_1.next
    while p_2:
        if p_2 in d:
            return d[p_2]
        p_2 = p_2.next
    return None


# O(N) time and O(1) using two pointers.  The key here is to iterate both pointers equal times over both LL and
# if there is an intersection between the two, it will happen at the same step.
def intersection(headA, headB):
    if not headA or not headB:
        return None
    p1, p2 = headA, headB
    len_a, len_b = 1, 1
    while p1.next:
        len_a += 1
        p1 = p1.next
    while p2.next:
        len_b += 1
        p2 = p2.next
    if p1 != p2:
        return None
    p1 = headB
    p2 = headA
    if len_a < len_b:
        for i in range(len_b - len_a):
            p1 = p1.next
    elif len_b < len_a:
        for i in range(len_a - len_b):
            p2 = p2.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


    return p1

[1]
[2,4,6,8,10,12,14,16,18,20,22]