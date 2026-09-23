from collections import defaultdict
import heapq

def prims(edges):

    graph = defaultdict(list)

    for u,v,w in edges:
        graph[u].append([v,w])
        graph[v].append([u,w])

    src = 0
    visited = set()
    total_cost = 0

    queue = [[0,src]]

    while queue:

        cost, node = heapq.heappop(queue)

        if node in visited:
            continue

        total_cost += cost
        visited.add(node)

        for nei_node, nei_cost in graph[node]:
            if nei_node not in visited:
                heapq.heappush(queue, [nei_cost, nei_node])

    return total_cost



    