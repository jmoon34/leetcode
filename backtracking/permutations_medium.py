# Given a collection of distinct integers, return all possible permutations.
#
# Example:
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# p([1]) = {p([1])} = [1]
# p([1,2]) = {p([1]) + p([2])} + {p([2]) + p([1])}
# p([1,2,3]) = {p([1]) + p([2,3])} + {p([2]) + p([1,3])} + {p([3]) + p([1,2])}
# As you can see from above, the key to solving this problem is that p(n) = p(i) + p(n-i) for all i in n
# This makes recursion the most natural way to solve the problem

def permute(nums):
    if len(nums) == 1:
        return [nums]
    sol = []
    for i in range(len(nums)):
        sub = permute([nums[j] for j in range(len(nums)) if j != i])
        for s in sub:
            sol.append([nums[i]] + s)
    return sol


# [1]
# [2,3]
def heaps_alg(nums):
    def backtrack(i=0):
        if i == n:
            solution.append(nums[:])
        for j in range(i, n):
            nums[i], nums[j] = nums[j], nums[i]
            backtrack(i+1)
            nums[i], nums[j] = nums[j], nums[i]
    solution = []
    n = len(nums)
    backtrack()
    return solution


def permutation_dfs(nums):
    def dfs(arr, sequence, sol):
        if not arr:
            sol.append(sequence)
        else:
            for i in range(len(arr)):
                dfs(arr[:i] + arr[i+1:], sequence + [arr[i]], sol)

    sol = []
    dfs(nums, [], sol)
    return sol





print(permutation_dfs([1,2,3,4]))



