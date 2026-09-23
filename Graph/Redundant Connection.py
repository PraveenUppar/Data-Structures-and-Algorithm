# You are given a connected undirected graph with n nodes labeled from 1 to n. 
# Initially, it contained no cycles and consisted of n-1 edges.

# We have now added one additional edge to the graph. 
# The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.

# The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the graph is still a connected non-cyclical graph. 
# If there are multiple answers, return the edge that appears last in the input edges.

from collections import defaultdict

def connection(edges):

    graph = defaultdict(list)

    def check(u, v, visited):

        if u == v:
            return True 

        visited.add(u)

        for nei_node in graph[u]:
            if nei_node not in visited:
                if check(nei_node, v, visited):
                    return True
        return False

    for u, v in edges:
        visited = set()
        if u in graph and v in graph and check(u,v,visited):
            return [u,v]
        graph[u].append(v)
        graph[v].append(u)


