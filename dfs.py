tree_adjacency = {
    1: [2, 3],
    2: [4, 5],
    3: [7, 8],
    4: [],
    5: [],
    7: [],
    8: []
}

def DFS_recurse_adjacency(tree, node):
    if len(tree[node]) == 0:
        return str(node)
    path = str(node)
    for n in tree[node]:
        path += DFS_recurse_adjacency(tree, n)
    return path


def DFS_iterative_adjacency(tree, root):
    stack = [root]
    seen = set([])
    path = ''
    while len(stack) != 0:
        node = stack.pop()
        if node in seen:
            continue
        path += str(node)
        seen.add(node)
        for n in tree[node]:
            stack.append(n)
    return path

def BFS_iterative_adjacency(tree, root):
    queue = [root]
    seen = set([])
    path = ''
    while len(queue) != 0:
        node = queue.pop(0)
        if node in seen:
            continue
        path += str(node)
        seen.add(node)
        for n in tree[node]:
            queue.append(n)
    return path


print DFS_recurse_adjacency(tree_adjacency, 1)
print DFS_iterative_adjacency(tree_adjacency, 1)
print BFS_iterative_adjacency(tree_adjacency, 1)

