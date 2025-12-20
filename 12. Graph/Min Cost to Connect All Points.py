class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        visited = set()
        total_cost = 0
        min_heap = [(0,0)]  # (curr_cost,curr_point)

        while (len(visited) < len(points)):

            curr_cost,curr_point = heapq.heappop(min_heap)

            if curr_point in visited:
                continue

            visited.add(curr_point)
            total_cost += curr_cost

            for next_point in range(len(points)):
                if next_point not in visited:
                    dist_cost = abs(points[curr_point][0] - points[next_point][0]) + abs(points[curr_point][1] - points[next_point][1]) 
                    heapq.heappush(min_heap,(dist_cost,next_point))

        return total_cost



        