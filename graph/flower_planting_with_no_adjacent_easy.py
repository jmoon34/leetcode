# You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.
#
# paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.
#
# Also, there is no garden that has more than 3 paths coming into or leaving it.
#
# Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.
#
# Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.
#
#
#
# Example 1:
#
# Input: N = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
# Example 2:
#
# Input: N = 4, paths = [[1,2],[3,4]]
# Output: [1,2,1,2]
# Example 3:
#
# Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# Output: [1,2,3,4]
#
#
# Note:
#
# 1 <= N <= 10000
# 0 <= paths.size <= 20000
# No garden has 4 or more paths coming into or leaving it.
# It is guaranteed an answer exists.

from collections import defaultdict
def planting_flowers(N, paths):
    g = defaultdict(list)
    for path in paths:
        g[path[0]].append(path[1])
        g[path[1]].append(path[0])
    colored = {}

    def dfs(g, v, colored):
        f_types = [1, 2, 3, 4]
        for neighbor in g[v]:
            if neighbor in colored:
                if colored[neighbor] in f_types:
                    f_types.remove(colored[neighbor])
        colored[v] = f_types[0]

    for v in range(1, N+1):
        dfs(g, v, colored)
    sol = []
    for v in range(N):
        sol.append(colored[v+1])
    return sol

x = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
print(planting_flowers(4, x))
