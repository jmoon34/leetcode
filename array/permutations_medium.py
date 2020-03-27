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

print(permute([1,2,3]))



