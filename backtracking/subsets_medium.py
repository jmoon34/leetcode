# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


def subset_rec(nums):
    n = len(nums)
    sol = [[]]
    for num in nums:
        sol += [curr + [num] for curr in sol]
        print(sol)
    return sol

def subset_backtrack(nums):
    sol = []
    def back_track(first=0, seq=[]):
        if len(seq) == n:
            sol.append(seq[:])
        for i in range(first, len(nums)):
            seq.append(nums[i])
            back_track(i+1, seq)
            seq.pop()
    for n in range(len(nums)+1):
        back_track()
    return sol


def s2(nums):
    sol = [[]]
    for num in nums:
        sol += [x + [num] for x in sol]
        print(sol)
    return sol

print(s2([1,2,3]))

