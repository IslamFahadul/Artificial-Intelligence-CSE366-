def dfs(g, start):
    visited = set()
    visited.add(start)
    stack = [start]
    while stack:
        current = stack.pop()
        print(current, end=" ")
        for neighbour in g[current]:
            if not neighbour in visited:
                visited.add(neighbour)
                stack.append(neighbour)

def dfs_route(g, start, target):
    visited = set()
    visited.add(start)
    stack = [start]
    parent = []
    found = False
    while stack:
        current = stack.pop()
        if current == target:
            parent.append(current)
            break
        print(current, end=" ")
        for neighbour in g[current]:
            if not neighbour in visited:
                visited.add(neighbour)
                stack.append(neighbour)

grap = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: [],
}
dfs(grap,1)