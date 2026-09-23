from collections import defaultdict


def topological(n, edges):

    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for nei_node in graph[node]:
            if nei_node not in visited:
                dfs(nei_node)

        stack.append(node)

    for i in range(n):
        if i not in visited:
            dfs(i)

    return stack[::-1]

