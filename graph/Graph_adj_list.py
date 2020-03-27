# Implementation of graphs using adjaceny list, which can easily be implemented using Python's collections.defaultdict


from collections import defaultdict, deque
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)

    def bfs(self, s):
        result = []
        q = deque()
        visited = [False for _ in range(len(self.nodes))]
        q.append(s)
        visited[s] = True
        while q:
            current = q.popleft()
            result.append(current)
            for adj_node in self.graph[current]:
                if not visited[adj_node]:
                    q.append(adj_node)
                    visited[adj_node] = True
        return result

    def dfs(self, s):
        result = []
        stack = [s]
        visited = [False for _ in range(len(self.nodes))]
        visited[s] = True
        while stack:
            current = stack.pop(-1)
            result.append(current)
            for node in self.graph[current]:
                if not visited[node]:
                    stack.append(node)
                    visited[node] = True

        return result

    def dfs_rec(self, s, visited=None):
        if not visited:
            visited = set()
        visited.add(s)
        print(s)
        for next in self.graph[s]:
            if next not in visited:
                self.dfs_rec(next, visited)
        return visited


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,4)
print(g.graph)


print(g.dfs_rec(0))
