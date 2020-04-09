from collections import defaultdict

x = [[0,(1,4)], [0,(7,8)], [1,(0,4)], [1,(7,11)], [1,(2,8)], [2,(1,8)], [2,(8,2)], [2,(3,7)], [2,(5,4)], [3,(2,7)], [3,(4,9)],
     [3,(5,14)], [4,(3,9)], [4,(5,10)], [5,(2,4)], [5,(3,14)], [5,(4,10)], [5,(6,2)], [6,(5,2)], [6,(7,1)], [6,(8,6)],
     [7,(0,8)], [7,(1,11)], [7,(6,1)], [7,(8,7)], [8,(2,2)], [8,(6,6)], [8,(7,7)]]

d = defaultdict(list)
for u, v in x:
    d[u].append(v)


def find_min(distances, visited):
    m = float('inf')
    u = 0
    for i in range(len(distances)):
        if not visited[i]:
            if distances[i] < m:
                m = distances[i]
                u = i
    return u

def dijkstra(g, n, start):
    visited = [False] * n
    parents = [None for _ in range(n)]
    distances = [float('inf')] * n
    distances[start] = 0
    for _ in range(n):
        u = find_min(distances, visited)
        visited[u] = True
        for v, d in g[u]:
            if not visited[v]:
                if distances[u] + d < distances[v]:
                    distances[v] = distances[u] + d
                    parents[v] = u

    for i in range(n):
        print("vertex:", i, "distance:", distances[i], "path:", end=" ")
        j = i
        p = [j]
        while parents[j] is not None:
            p.append(parents[j])
            j = parents[j]
        p.reverse()
        print(p)

    return distances, parents



print(dijkstra(d, 9, 0))