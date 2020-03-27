# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is
# closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# [-4, -1, 1, 2]
def three_sum_closest(nums, target):
    import sys
    list.sort(nums)
    closest_sum = sys.maxsize
    min_distance = sys.maxsize
    for i in range(len(nums)):
        l = i+1
        r = len(nums)-1
        while l < r:
            distance = target - (nums[i] + nums[l] + nums[r])
            print(distance, min_distance)
            if abs(distance) < abs(min_distance):
                min_distance = distance
                closest_sum = nums[i] + nums[l] + nums[r]
            if distance > 0 :
                l += 1
            elif distance == 0:
                return target
            else:
                r -= 1
    return min_distance, closest_sum

print(three_sum_closest([-1,-1,1,1,3], -1))
