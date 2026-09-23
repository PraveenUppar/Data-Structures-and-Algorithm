def bellmanFord(n ,edges):

    src = 0
    dist = [float("inf")] * n
    dist[src] = 0

    for _ in range(n - 1):
        for u,v,w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v] :
                dist[v] = dist[u] + w

    return dist