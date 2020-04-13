# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


def missing_number(nums):
    x = {i for i in range(len(nums)+1)}
    print(x)
    for num in nums:
        x.remove(num)
    return x

def missing_number_bit(nums):
    sol = len(nums)
    for i in range(len(nums)):
        sol ^= i ^ nums[i]
    return sol

def missing_number_math(nums):
    # sum(1,2,...n) = n(n+1)//2
    return (len(nums)*(len(nums)+1)//2) - sum(nums)

print(missing_number_math([3,0,1]))