# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.

def intersection_set(num1, num2):
    return {x for x in num1 if x in num2}


def intersection_pointer(nums1, nums2):
    list.sort(nums1)
    list.sort(nums2)
    intersection = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        a, b = nums1[i], nums2[j]
        if a == b:
            intersection.append(nums1[i])
            while i < len(nums1) and nums1[i] == a:
                i += 1
            while j < len(nums2) and nums2[j] == b:
                j += 1
        elif a < b:
            while i < len(nums1) and nums1[i] == a:
                i += 1
        elif a > b:
            while j < len(nums2) and nums2[j] == b:
                j += 1

    return intersection

print(intersection_pointer([1,3,2,5,3,2], [4,2,3,3,5]))

