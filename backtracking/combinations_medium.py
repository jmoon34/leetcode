# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# [1,2,3,4]
# Time complexity is O(k * nCk) where nCk is n!/(n-k)!k!  There are nCk total combinations and it takes k amount of work to build each of them
# as a sequence
# Space complexity is O(nCk) since there are that many combinations
# This is a backtracking approach where you pick a starting point and add => method call with next index => remove
def combinations_back_track(n, k):
    def back_track(start=0, seq=[]):
        print(seq)
        if len(seq) == k:
            sol.append(seq[:])
            return
        for s in range(start, n):
            seq.append(s+1)
            back_track(s+1, seq)
            seq.pop()
    sol = []
    back_track()
    return sol

# dfs approach where the idea is same as the backtracking, but the forloop portion is taken cared of by the increasingly smaller array
# if the recursive call were to be dfs(arr[:i] + arr[i+1], ...) it would return all permutations, but calling it with just the
# latter portion of the array allows it to become a combination (excludes element from the front)
def combinations_dfs(n, k):
    a = [i for i in range(1, n+1)]
    def dfs(arr, seq, sol):
        if len(seq) == k:
            sol.append(seq)
            return
        for i in range(len(arr)):
            dfs(arr[i+1:], seq + [arr[i]], sol)
    sol = []
    dfs(a, [], sol)
    return sol


# Copied from solution section.  Works by generating an increasing sequence of binary number where each digit is mapped to numbers in list(range(1, n+1))
# where 1 means it's in the sequence and 0 means it's not.
def lexicographic_sorting(n, k):
    nums = [i for i in range(1, k+1)] + [n+1]
    sol = []
    j = 0
    while j < k:
        sol.append(nums[:k])
        j = 0
        while j < k and nums[j+1] == nums[j] + 1:
            nums[j] = j + 1
            j += 1
        nums[j] += 1
        print(nums)
    return sol


print(lexicographic_sorting(4, 2))