# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each
# nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]

# Example 3:
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
#
# Constraints:
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

def smaller_nums_slow(nums):
    sol_array = [0 for _ in range(len(nums))]
    for i, u in enumerate(nums):
        for j, v in enumerate(nums):
            if i == j:
                continue
            if v < u:
                sol_array[i] += 1
    return sol_array

# [1, 2, 2, 3, 8]
def smaller_nums_sort(nums):
    copy = nums[:]
    list.sort(copy)
    print(nums, copy)
    sol = []
    for i in range(len(nums)):
        sol.append(bin_search_lowest_index(copy, nums[i]))
    return sol


def bin_search_lowest_index(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# counts = [0, 1, 2, 1, 0, 0, 0, 0, 1]
# less_than = [0, 0, 1, 3, 4, 4, 4, 4, 4]
def smaller_nums(nums):
    counts, less_than = [0] * 101, [0] * 101
    for i, x in enumerate(nums):
        counts[x] += 1
    for i in range(1, 101):
        less_than[i] = counts[i-1] + less_than[i-1]



print(smaller_nums_sort([8,1,2,2,3]))