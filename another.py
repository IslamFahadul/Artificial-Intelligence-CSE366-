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