# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.

from collections import defaultdict

def tree(n, edges):

    if len(edges) != n - 1:
        return False

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def check(node):

        visited.add(node)

        for nei_node in graph[node]:
            if nei_node not in visited:
                check(nei_node)
        
    check(0)

    if len(visited) != n:
        return False 

    return True