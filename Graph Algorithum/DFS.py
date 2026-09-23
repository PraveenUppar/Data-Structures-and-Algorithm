from collections import defaultdict

def dfsGraph(n, edges):

    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    res = []

    def dfs(node):

        visited.add(node)
        res.append(node)

        for nei_node in graph[node]:
            if nei_node not in visited:
                dfs(nei_node)
    dfs(0)
    return res



