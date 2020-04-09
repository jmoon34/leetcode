# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]


# Output: 4


def single_number_with_memory(nums):
    m = {}
    for i in range(len(nums)):
        if nums[i] not in m:
            m[nums[i]] = 1
        else:
            m[nums[i]] += 1
    for num in m:
        if m[num] == 1:
            return num

def single_number_const_memory(nums):
    a = 0
    for num in nums:
        a ^= num
    return a