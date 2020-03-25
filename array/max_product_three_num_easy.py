# Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
# Example 1:
#
# Input: [1,2,3]
# Output: 6
#
#
# Example 2:
#
# Input: [1,2,3,4]
# Output: 24
#
#
# Note:
#
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

def three_max_product(nums):
    first_three = nums[:3]
    a, c = min(first_three), max(first_three)
    first_three.remove(a)
    first_three.remove(c)
    b = first_three[0]
    m, n = a, b
    for i in range(3, len(nums)):
        if nums[i] > c:
            a = b
            b = c
            c = nums[i]
        elif b < nums[i] <= c:
            a = b
            b = nums[i]
        elif a < nums[i] <= b:
            a = nums[i]

        if nums[i] < m:
            n = m
            m = nums[i]
        elif m <= nums[i] < n:
            n = nums[i]
        print(m, n, a,b,c)
    return max(a*b*c, c*m*n)


def nlogn(nums):
    list.sort(nums)
    return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])



print(three_max_product([-5,-4,-1,1,50]))



