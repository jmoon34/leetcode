# Given a directed graph, the task is to complete the method isCyclic() to detect if there is a cycle in the graph or not.
# You should not read any input from stdin/console. There are multiple test cases. For each test case, this method will be called individually.
#
# Input: The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' test cases
# follow. Each test case consists of two lines. Description of testcases is as follows: The First line of each test
# case contains two integers 'N' and 'M'  which denotes the no of vertices and no of edges respectively.
# The Second line of each test case contains 'M'  space separated pairs u and v denoting that there is an uni-directed  edge from u to v .
#
# Output:
# The method should return 1 if there is a cycle else it should return 0.
#
# User task:
# Since this is a functional program you don't have to worry about input, you just have to complete the function
#
# Constraints:
# 1 <= T <= 1000
# 1<= N,M <= 1000
# 0 <= u,v <= N-1
#
# Example:
# Input:
# 3
# 2 2
# 0 1 0 0
# 4 3
# 0 1 1 2 2 3
# 4 3
# 0 1 2 3 3 2
# Output:
# 1
# 0
# 1
#
# Explanation:
# Testcase 1: In the above graph there are 2 vertices. The edges are as such among the vertices.
#
#
# From graph it is clear that it contains cycle.


from collections import defaultdict


def is_cyclic_rec(g, N):
    visited = [False] * N
    rec_stack = [False] * N
    for node in range(N):
        if not visited[node]:
            if recurse(node, g, visited, rec_stack):
                return True
    return False

def recurse(v, g, visited, rec_stack):
    visited[v] = True
    rec_stack[v] = True
    for neighbor in g[v]:
        if not visited[neighbor]:
            if recurse(neighbor, g, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
    rec_stack[v] = False
    return False




g = defaultdict(list)
# N, M = map(int, input().split())
# print(N, M)
# edges = [int(x) for x in input().split()]
N, M = 6, 7
edges = [0,1,1,2,2,3,4,1,4,3,1,3,3,1]
for i in range(M):
    g[edges[2*i]].append(edges[2*i+1])
print(g)
print(is_cyclic_iter(g, N))
print(is_cyclic_rec(g, N))
