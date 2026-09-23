from collections import defaultdict
from collections import deque

def bfsGraph(n,edges):

    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    res = []

    queue = deque([0])

    while queue:

        node = queue.popleft()
        res.append(node)

        for nei_node in graph[node]:
            if nei_node not in visited:
                visited.add(nei_node)
                queue.append(nei_node)

    return res

