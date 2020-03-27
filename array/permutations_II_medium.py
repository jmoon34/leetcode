# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# slightly modified the solution of permutations_medium.py using tuples and sets to fix the duplicate problem
def permuteUnique(nums):
    if len(nums) == 1:
        return ((nums[0],),)
    sol = set()
    for i in range(len(nums)):
        sub = permuteUnique([nums[j] for j in range(len(nums)) if j != i])
        for s in sub:
            sol.add(tuple((nums[i],) + s))
    return sol


# A similar method of solving this problem using a depth-first-search approach
def permute_unique_2(nums):
    if not nums:
        return []
    def dfs(nums, sequence, sol):
        if not nums:
            sequence = tuple(sequence)
            if sequence not in sol:
                sol.add(sequence)
            return
        else:
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], sequence + [nums[i]], sol)
    sol = set()
    dfs(nums, [], sol)
    return sol


