# You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

# ui is the source node (an integer from 1 to n)
# vi is the target node (an integer from 1 to n)
# ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
# You are also given an integer k, representing the node that we will send a signal from.

# Return the minimum time it takes for all of the n nodes to receive the signal. 
# If it is impossible for all the nodes to receive the signal, return -1 instead.

from collections import defaultdict
import heapq

def network(edges, n, src):

    graph = defaultdict(list)

    for u,v,w in edges:
        graph[u].append([v,w])

    dist = [float("inf")] * n + 1
    dist[src] = 0

    queue = [[0, src]]

    while queue:
        curr_dist, node = heapq.heappop(queue)

        if curr_dist > dist[node]:
            continue

        for nei_node, nei_dist in graph[node]:
            if nei_dist + curr_dist < dist[nei_node]:
                dist[nei_node] = curr_dist + nei_dist
                heapq.heappush(queue, [dist[nei_dist], nei_node])

    max_time = max(dist)

    if max_time == float("inf"):
        return -1
    else:
        return max_time


