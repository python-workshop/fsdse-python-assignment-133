def get_neighbors(x):
    if x == 'a':
        return ['b', 'c']
    if x == 'b':
        return ['d', 'e']
    if x == 'c':
        return []
    if x == 'd':
        return ['f']


    return [] # Other nodes have no neighbors.

def bfs(start):
    queue = [start]
    visited = set(start)

    while queue:
        node = queue.pop(0)

        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return visited

print(str(bfs('e')))

