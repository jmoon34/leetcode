# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# [1,3,4,13,9,8,21,5], target = 34
def two_sum_max(nums, target):
    for i in range(len(nums)-1):
        base = nums[i]
        complement = target - base
        for j in range(i+1, len(nums)):
            if nums[j] == complement:
                return [i, j]
    return -1


def twoSum(nums, target):
    mapping = {}
    for i in range(len(nums)):
        if nums[i] in mapping:
            return mapping[nums[i]], i
        mapping[target - nums[i]] = i
    return -1

print(twoSum([2, 7, 11, 15], 9))
