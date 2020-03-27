# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

def three_sum(nums):
    sol = set()
    for i in range(len(nums)):
        a = nums[i]
        target = -a
        m = {}
        for j in range(i+1, len(nums)):
            b = nums[j]
            print(a, b, m)
            if b in m:
                triplet = tuple(sorted([a, m[b], b]))
                sol.add(triplet)
            else:
                m[target-b] = b
    return sol


def three_sum_two(nums):
    sol = set()
    list.sort(nums)
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = len(nums)-1
        while l < r:
            if nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
            else:
                sol.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
    return sol
# [-4,-1,-1,0,1,2]
print(three_sum_two([-1,0,1,2,-1,-4]))
