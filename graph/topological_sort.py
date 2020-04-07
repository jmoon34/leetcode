from collections import deque, defaultdict





# recursve depth-first-search given adjacency list representation of graph
def dfs_recursive(g, n):
    visited = set()
    result = []
    def recurse(node):
        visited.add(node)
        result.append(node)
        for neighbor in g[node]:
            if neighbor not in visited:
                recurse(neighbor)
    for start in range(n):
        if start not in visited:
            recurse(start)
    return result

# modifying recursive depth-first-search slightly to make it a topological sort
def topological_sort_def(g, n):
    result = []
    visited = set()
    def recurse(node):
        visited.add(node)
        for neighbor in g[node]:
            if neighbor not in visited:
                recurse(neighbor)
        result.insert(0, node) # for better efficieny, make this result.append() and
    for start in range(n):
        if start not in visited:
            recurse(start)
    return result # make this return result[::-1]


# topological sort using Kahn's algorithm
def khan_topological_sort(g, n):
    num_inc_edges = {i: 0 for i in range(n)}
    for i in g:
        for j in g[i]:
            num_inc_edges[j] += 1 # creates a dictionary that counts how many edges are directed at it
    q = deque()
    for i in range(n):
        if num_inc_edges[i] == 0:
            q.append(i) # populate the queue with leaf nodes
    result = []
    while q:
        print(q)
        current = q.popleft()
        result.append(current)
        for node in g[current]:
            num_inc_edges[node] -= 1
            if num_inc_edges[node] == 0:
                q.append(node)
    if max(num_inc_edges.values()) > 0:
        raise AttributeError("Cycle detected, topological sort impossible")
    return result


# iterative version of depth-first-search
def dfs_iter(g, n):
    visited = [False] * n
    result = []
    for start in range(n):
        if not visited[start]:
            stack = [start]
            visited[start] = True
            while stack:
                current = stack.pop()
                result.append(current)
                for neighbor in g[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
    return result

edge = [[0,1],[1,2],[1,3],[1,5],[3,2],[2,4],[0,5]]
g = defaultdict(list)
for u, v in edge:
    g[u].append(v)

print(g)
print(topological_sort_def(g, 6))
print(khan_topological_sort(g, 6))