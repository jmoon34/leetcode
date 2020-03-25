import sys
import heapq

class Vertex:
    def __init__(self, name):
        self.name = name
        self.distance = sys.maxsize
        self.visited = False
        self.neighbors = {}
        self.previous = None

    def get_distance(self):
        return self.distance

    def set_distance(self, d):
        self.distance = d

    def get_name(self):
        return self.name

    def add_neighbor(self, node, weight=0):
        self.neighbors[node] = weight

    def get_distance_to_neighbor(self, node):
        return self.neighbors[node]

    def set_previous(self, node):
        self.previous = node

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.name) + ', neighbors: ' + str([x.name for x in self.neighbors])

    def __repr__(self):
        return str(self)

class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, name):
        v = Vertex(name)
        self.vertices[name] = v
        self.num_vertices += 1
        return v

    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        self.vertices[u].add_neighbor(self.vertices[v], weight)
        self.vertices[v].add_neighbor(self.vertices[u], weight)

    def get_vertex(self, name):
        if name in self.vertices:
            return self.vertices[name]
        else:
            return None

    def get_vertices(self):
        return self.vertices.keys()


    @staticmethod
    def rebuild_path(vertex, path):
        if vertex.previous:
            path.append(vertex.previous.get_name())
            Graph.rebuild_path(vertex.previous, path)
        return

    @staticmethod
    def dijkstra(graph, start):
        start.set_distance(0)
        unvisited_queue = [(v.get_distance(), id(v), v) for v in graph]
        heapq.heapify(unvisited_queue)

        while unvisited_queue:
            current = heapq.heappop(unvisited_queue)[2]
            print(current, unvisited_queue)
            current.set_visited()
            for neighbor in current.neighbors:
                print(neighbor)
                if neighbor.visited:
                    continue
                new_distance = current.get_distance() + current.get_distance_to_neighbor(neighbor)
                if new_distance < neighbor.get_distance():
                    print("updated:", neighbor.name, new_distance)
                    neighbor.set_distance(new_distance)
                    neighbor.set_previous(current)

            while unvisited_queue:
                heapq.heappop(unvisited_queue)
            unvisited_queue = [(v.get_distance(), id(v), v) for v in graph if not v.visited]
            heapq.heapify(unvisited_queue)





g = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')
g.add_edge('a', 'b', 7)
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

Graph.dijkstra(g, g.get_vertex('a'))
target = g.get_vertex('e')
path = [target.get_name()]
Graph.rebuild_path(target, path)
print ('The shortest path : %s' %(path[::-1]))