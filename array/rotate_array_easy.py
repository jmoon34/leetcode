# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:
#
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# O(n) time, O(1) space. Cyclical swapping going through n elements
# Important thing to note here is that simply starting from 0 and jumping by k may not cover
# all the elements.  e.g. len(num) = 6, k = 2  ==> 0,2,4,0,2,4... missing swap between 1 and 3
# Therefore it is necessary to iterate through starting points and stop when all elements have been cycled (count == len(num))
def rotate_in_place_by_k_fast(nums, k):
    count, start = 0, 0
    while count < len(nums):
        i = start
        prev = nums[i]
        while True:
            temp = nums[(i+k) % len(nums)]
            nums[(i+k) % len(nums)] = prev
            prev = temp
            i = (i+k) % len(nums)
            count += 1
            if i == start:
                break
        start += 1
    print(nums)


# O(n) time, O(1) space
# First reverse the entire array
# Then reverse the first k elements
# Finally reverse the leftover n-k elements
def rotate_by_reversing(nums, k):
    k = k % len(nums)
    for i in range(len(nums)//2):
        nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
    for i in range(k//2):
        nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
    for i in range(k, (len(nums)+k)//2):
        nums[i], nums[len(nums)-1-i+k] = nums[len(nums)-1-i+k], nums[i]
    print(nums)

#rotate_in_place_by_k_fast([1,2,3,4,5,6], 2)
rotate_by_reversing([1,2], 3)
# perform rotating once k times, O(n*k), time limit exceeded with large input
def rotate_in_place_by_k_slow(nums, k):
    temp = 0
    prev = nums[0]
    for i in range(k):
        for j in range(1, len(nums)):
            temp = nums[j]
            nums[j] = prev
            prev = temp
        nums[0] = prev
    print(nums)



# O(n) time for the insertions in extend, O(n) space for the extra array
def rotate_by_k_1(nums, k):
    left = nums[:len(nums)-k]
    right = nums[len(nums)-k:]
    right.extend(left)
    return right



