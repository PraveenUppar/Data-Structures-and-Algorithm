# You are given a 2-D integer array points, where points[i] = [xi, yi]. 
# Each points[i] represents a distinct point on a 2-D plane.

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

# Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

from collections import defaultdict
import heapq


def connectpoints(points):

    n = len(points)
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            graph[i].append([j, cost])
            graph[j].append([i, cost])

    visited = set()
    total_cost = 0

    queue = [[0,0]]
    
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
    
    