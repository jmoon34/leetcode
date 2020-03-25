# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2


def majority(nums):
    counts = {}
    half = len(nums) // 2
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    for num, count in counts.items():
        if count > half:
            return num


# [2,2,1,1,1,2,2]                   [1,2,1,2,2,1,2]
# [2,2,1,1] [1,2,2]                 [1,2,1,2] [2,1,2]
# [2,2] [1,1]  [1,2] [2]            [1,2] [1,2]  [2,1] [2]
def majority_recursion(nums):
    def maj_r(low, high):
        if low == high:
            return nums[low]
        mid = (low + high) // 2
        left = maj_r(low, mid)
        right = maj_r(mid+1, high)

        if left == right:
            return left

        left_count = sum([1 for i in range(low, high+1) if nums[i] == left])
        right_count = sum([1 for i in range(low, high+1) if nums[i] == right])
        return left if left_count > right_count else right


    return maj_r(0, len(nums)-1)




print(majority([3,2,3]))