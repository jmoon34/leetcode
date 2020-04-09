# Implementation of graphs using an adjacency matrix.
# Implementation of Dijkstra's algorithm: not as efficient as writing a class for Vertex (refer to Graph_vertex.py)
# since we can't use a min-heap and have to use the utility function min_distance()
import sys
import heapq
class Graph_adj_matrix:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def min_distance(self, dist, span_set):
        min = sys.maxsize
        for v in range(self.v):
            if dist[v] < min and not span_set[v]:
                min = dist[v]
                min_index = v
        return min_index

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.v):
            print(node, "\t", dist[node])

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.v
        dist[src] = 0
        span_set = [False] * self.v

        for cout in range(self.v):
            u = self.min_distance(dist, span_set)
            span_set[u] = True
            for v in range(self.v):
                if self.graph[u][v] > 0 and not span_set[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)



g = Graph_adj_matrix(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

g.dijkstra(0)
