class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = {i: [] for i in range(n)}
        for s, d, p in flights:
            adj[s].append((d, p))

        pq = [(0, src, 0)]
        
        min_stops = [float('inf')] * n
        
        while pq:
            cost, u, stops = heapq.heappop(pq)
            
            if u == dst:
                return cost
            
            if stops > k:
                continue
            
            if stops >= min_stops[u]:
                continue
                
            min_stops[u] = stops
            
            for v, w in adj[u]:
                heapq.heappush(pq, (cost + w, v, stops + 1))
                
        return -1

