class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        row = len(grid) 
        cols = len(grid[0])

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visited = set()
        visited.add((0,0))

        min_heap = [(grid[0][0],0,0)]
        res_time = 0

        while min_heap:
            curr_height,r,c = heapq.heappop(min_heap)
            res_time = max(res_time,curr_height)

            if r == row - 1 and c == cols - 1:
                return res_time
            
            for dr,dc in dirs:
                new_r = r + dr
                new_c = c + dc
                if (new_r < 0 or new_c < 0 or new_r == row or new_c == cols or (new_r, new_c) in visited):
                    continue
                visited.add((new_r,new_c))
                heapq.heappush(min_heap, (grid[new_r][new_c], new_r, new_c))

        return res_time