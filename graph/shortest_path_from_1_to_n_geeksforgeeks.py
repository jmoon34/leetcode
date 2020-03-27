# Consider a directed graph whose vertices are numbered from 1 to n. There is an edge from
# a vertex i to a vertex j iff either j = i + 1 or j = 3i. The task is to find the minimum number of edges in a path
# in G from vertex 1 to vertex n.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
#
# Each test case contains a value of n.
#
# Output:
# Print the number of edges in the shortest path from 1 to n.
#
# Constraints:
# 1<=T<=30
# 1<=n <=1000
#
# Example:
# Input:
# 2
# 9
# 4
#
# Output:
# 2
# 2



# Preferable solution for this question that doesn't really require graphs.  Use dynamic programming
# j = 3i or j = i + 1
# j+1 = 3(i+1)
# j = 3i +2
# [0, 1, 2, 1, 2
def shortest_path_to_n(n):
    steps = [0 for _ in range(n)]
    steps[1], steps[2] = 1,1
    for i in range(3, n):
        if (i-2) % 3 == 0:
            steps[i] = min(steps[i-1] + 1, steps[(i-2)//3] + 1)
        else:
            steps[i] = steps[i-1] + 1
    return steps



# Solving using adjacency matrix and Dijkstra's algorithm, but memory overload for large n
import sys
class Graph:
    def __init__(self, num_vertices):
        self.matrix = [[1 if (col == row + 1 or col == 3*row + 2) else 0
                        for col in range(num_vertices)] for row in range(num_vertices)]
        self.num_vertices = num_vertices

    def get_min_index(self, distances, visited):
        min = sys.maxsize
        for i in range(self.num_vertices):
            if distances[i] < min and not visited[i]:
                min = distances[i]
                min_index = i
        return min_index

    def dijkstra(self, start=0):
        distances = [sys.maxsize] * self.num_vertices
        distances[start] = 0
        visited = [False] * self.num_vertices

        for _ in range(self.num_vertices):
            u = self.get_min_index(distances, visited)
            visited[u] = True
            for v in range(self.num_vertices):
                if not visited[v] and self.matrix[u][v] > 0:
                    new_distance = distances[u] + self.matrix[u][v]
                    distances[v] = min(distances[v], new_distance)
        return distances

g = Graph(1000)
steps = g.dijkstra()
print(steps)
print(shortest_path_to_n(1000))
# num_test_cases = int(input())
# for i in range(num_test_cases):
#     n = int(input())
#     print(steps[n-1])


