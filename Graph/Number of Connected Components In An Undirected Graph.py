# You have an undirected graph of n nodes labeled from 0 to n - 1. 
# You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

# Return the number of connected components in the graph.

from collections import defaultdict

def connected(n, edges):

    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    res = 0
    visited = set()

    def check(node):

        visited.add(node)

        for nei_node in graph[node]:
            if nei_node not in visited:
                check(nei_node)

    for i in range(n):
        if i not in visited:
            check(i)
            res += 1

    return res
