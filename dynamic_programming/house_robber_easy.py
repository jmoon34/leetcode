# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
# money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.


# Have to check i-2 AND i-3 since we can rob every other house, there's a chance that i-3 has higher value than i-2
# e.g. [2,1,1,2] => [2,1,3,3] if we only check i-2 but [2,1,1,2] => [2,1,3,4] if we check i-2 and i-3
# We don't need to check i-4 because i-4 is not exclusive from i-2, meaning we can just rob both
# e.g. [2,1,1,1,2] => [2,1,3,3,5]
def house_robber(nums):
    if not nums:
        return 0
    max_money = nums[:]
    for i in range(2, len(nums)):
        max_money[i] += max_money[i - 2] if i < 3 else max(max_money[i - 2], max_money[i - 3])
    return max(max_money)

print(house_robber([2,7]))
print(house_robber([2,5,1,1,1,2]))
