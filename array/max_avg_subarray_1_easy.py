# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average
# value. And you need to output the maximum average value.
#
# Example 1:
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
#
#
# Note:
#
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].


def max_avg_subarray(nums, k):
    rolling_sum = sum([nums[i] for i in range(k)])
    max_sum = rolling_sum
    for i in range(1, len(nums)-k+1):
        print(rolling_sum)
        rolling_sum -= nums[i-1] - nums[i+k-1]
        max_sum = max(max_sum, rolling_sum)
    return max_sum / k

print(max_avg_subarray([1,12,-5,-6,50,3], 6))
