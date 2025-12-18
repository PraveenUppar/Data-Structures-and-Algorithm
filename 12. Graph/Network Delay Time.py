class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))

        visited = set()

        # In Python's heapq, tuples are sorted by their first element.
        min_heap = [(0,k)]

        while min_heap:
            (curr_time,curr_node) = heapq.heappop(min_heap)

            if curr_node in visited:
                continue

            visited.add(curr_node)

            if len(visited) == n:
                return curr_time
            
            for nei_node, nei_time in adj[curr_node]:
                if nei_node not in visited:
                    new_time = curr_time + nei_time
                    heapq.heappush(min_heap,(new_time, nei_node))  
        return -1