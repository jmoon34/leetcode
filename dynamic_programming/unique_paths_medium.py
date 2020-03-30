# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
# corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
# Example 2:
# Input: m = 7, n = 3
# Output: 28
#
# Constraints:
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

# 1 x 1: 0
# 1 x 2: r => 1
# 2 x 2: rd, dr => 2
# 3 x 2: rdd, drd, ddr

# Dynamic programming based on the fact that unique paths to (i,j) is the sum of paths to (i-1,j) and (i,j-1)
def unique_paths(m, n):
    paths = [[1 for col in range(n)] for row in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
    return paths[m-1][n-1]

print(unique_paths(7, 3))