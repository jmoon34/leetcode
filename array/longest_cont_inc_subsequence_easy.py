# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.

# [1,2,4,3,5,7,8,1,4]
def longest_inc_sub(nums):
    if not nums:
        return 0
    sub_len = [1 for _ in range(len(nums))]
    sub_index = 0
    max_len = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            sub_len[sub_index] += 1
            max_len = max(max_len, sub_len[sub_index])
        else:
            sub_index = i
    return max_len

print(longest_inc_sub([1,3,5,7]))