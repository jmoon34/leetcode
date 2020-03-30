# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# [-2,1,-3,4,-1,2,1,-5,4]
# [-2,1,-2,
def max_subarray(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i-1] + nums[i], nums[i])
    return max(nums)

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
