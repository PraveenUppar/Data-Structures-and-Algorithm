from collections import defaultdict
import heapq

def dijsktra(n, edges):

    graph = defaultdict(list)

    for u,v,w in edges:
        graph[u].append([v,w])
        graph[v].append([u,w])

    src = 0
    res = [float("inf")] * n
    res[src] = 0

    queue = [[0, src]]

    while queue:
        dist, node = heapq.heappop(queue)

        if dist > res[node]:
            continue

        for nei_node, nei_dist in graph[node]:
            if nei_dist + res[node] < res[nei_node]:
                res[nei_node] = nei_dist + res[node]
                heapq.heappush(queue, [res[nei_node], nei_node])

    return res

