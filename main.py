# library
from pyvis.network import Network as G
import networkx as nx
# map<int, list>
# node -> neighbour

# static graph
grap = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: [],
}

# dynamic graph
# graph builder
print("Build A Graph First")
nodes = list(map(int, input("Enter The Nodes:").split()))
print("Enter The Edges: (Tip: Assign None to both left and right vertices to denote there are no edges left)")
graph = {}
for n in nodes:
    graph[n] = []
while True:
    lf, rg = list(map(int, input("There is an edge between:").split()))
    if lf == -1 and rg == -1:
        break
    else:
        graph[lf].append(rg)
print(graph) 


# bfs graph traversal
def bfs_traverse(g, start):
    q = []
    visited = set()
    q.append(start)
    visited.add(start)
    while len(q):
        current = q.pop(0)
        print(current, end=" ")
        for neighbour in g[current]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)

# bfs_traverse(grap, 1)
# 5
# bfs_search
def bfs_search(g, start, target):
    q = []
    visited = set()
    parent = {}
    q.append(start)
    visited.add(start)
    parent[start] = None
    found = False
    while len(q):
        current = q.pop(0)
        if current == target:
            found = True
            break
        for neighbour in g[current]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)
                parent[neighbour] = current
    # path recontruction
    path = []
    if found:
        path.append(target)
        while parent[target] is not None:
            path.append(parent[target])
            target = parent[target]
        path.reverse()
    return path
start_node = int(input("Enter start node: "))
target_node = int(input("Enter target node: "))
search_result = bfs_search(graph, start_node, target_node)

# 6 graph visualization
g = G()
# graph
for key in graph:
        g.add_node(key)
for key, val in graph.items():
    if val:
        for v in val:
            g.add_edge(key, v)

# result
# for key in graph:
#     if key in search_result:
#         g.add_node(key, color="green") # BFS SEARCH RESULT
#     else:
#         g.add_node(key)
# for key, val in graph.items():
#     if val:
#         for v in val:
#             g.add_edge(key, v)
            # print(key, v)

g.show("basic.html")
