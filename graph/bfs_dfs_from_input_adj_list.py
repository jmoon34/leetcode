# Given N and E, the number of nodes and edges in a directed graph. The task is to do Breadth First Search of this graph.
#
# Input:
# The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' test cases follow.
# Each test case consists of two lines. Description of testcases is as follows: The First line of each test case contains
# two integers 'N' and 'E'  which denotes the no of vertices and no of edges respectively. The Second line of each test
# case contains 'E'  space separated pairs u and v denoting that there is a edge from u to v .
#
# Output:
# For each testcase, print the BFS of the graph starting from 0.
#
# Note: The expected output button always produces BFS starting from node 0.
#
# User Task:
# Since, this is a functional problem, your task is to complete the function bfs() which do BFS of the given graph
# starting from node 0 and prints the nodes in BFS order.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100
#
# Example:
# Input:
# 2
# 5 4
# 0 1 0 2 0 3 2 4
# 3 2
# 0 1 0 2
#
# Output:
# 0 1 2 3 4    // BFS from node 0
# 0 1 2
#
# Explanation:
# Testcase 1:
# 0 is connected to 1 , 2 , 3
# 2 is connected to 4
# so starting from 0 , bfs will be 0 1 2 3 4.

from collections import defaultdict, deque



# bfs starting from node 0
def bfs(g, N):
    q = deque()
    visited = [False] * N
    q.append(0)
    visited[0] = True
    while q:
        current = q.popleft()
        print(current, end=" ")
        for next in g[current]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

# dfs starting from node 0
def dfs(g, N):
    stack = []
    visited = [False] * N
    stack.append(0)
    visited[0] = True
    while stack:
        current = stack.pop(-1)
        print(current, end=" ")
        for next in g[current]:
            if not visited[next]:
                stack.append(next)
                visited[next] = True


def dfs_recursive(g, N):
    visited = [False] * N
    dfs_recurse(0, g, visited)

def dfs_recurse(s, g, visited):
    print(s, end=" ")
    visited[s] = True
    for node in g[s]:
        if not visited[node]:
            dfs_recurse(node, g, visited)

edge = [int(x) for x in input().split()]
print(edge)
g = defaultdict(list)
for i in range(len(edge)):
    if i % 2 == 1:
        g[edge[i-1]].append(edge[i])

bfs(g, 5)