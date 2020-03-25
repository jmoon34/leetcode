# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2),
# ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Example 1:
# Input: [1,4,3,2]
#
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].

# In order to maximize sum of min(ai, bi), we need to minimize the difference between ai and bi
# Question turns into pairing numbers that are closest to each other
# [-3,-1,2,4,5,8,10,12] => -3 + 2, 5, 10
def array_partition(nums):
    return sum(x for x in sorted(nums)[::2])

print(array_partition([-3,-1,2,4,5,8,10,12]))

nums = [-3,-1,2,4,5,8,10,12]
print(nums)

