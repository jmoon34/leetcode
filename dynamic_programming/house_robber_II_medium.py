# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent
# houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# [1,2,1,1,2]
# [1,2,2,3,4]
def house_robber(nums):
    if not nums:
        return 0
    if len(nums) <= 3:
        return max(nums)
    max_with_first = nums[:-1]
    max_without_first = nums[1:]
    for i in range(2, len(max_with_first)):
        max_with_first[i] += max_with_first[i-2] if i == 2 else max(max_with_first[i-2], max_with_first[i-3])
        max_without_first[i] += max_without_first[i - 2] if i == 2 else max(max_without_first[i - 2], max_without_first[i - 3])
    return max(max(max_with_first), max(max_without_first))

print(house_robber([2,1,2,6,1,8,10,10]))
print(house_robber([2,2,4,3,2,5]))
print(house_robber([0]))