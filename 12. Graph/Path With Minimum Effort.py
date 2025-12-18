class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        row = len(heights)
        cols = len(heights[0])

        min_heap = [(0,0,0)]  #(effort, row, col)

        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        max_effort = 0
        visited = set()

        if heights is None:
            return 0

        while min_heap:
            effort, curr_row, curr_cols = heapq.heappop(min_heap)

            max_effort = max(max_effort, effort)

            if (curr_row, curr_cols) == (row - 1,cols - 1):
                return max_effort
            
            visited.add((curr_row,curr_cols))

            for dr,dc in dirs:
                new_row = curr_row + dr
                new_cols = curr_cols + dc

                if (new_row, new_cols) not in visited and 0 <= new_row < row and 0 <= new_cols < cols:
                    new_effort = abs(heights[new_row][new_cols] - heights[curr_row][curr_cols])
                    heapq.heappush(min_heap,(new_effort,new_row,new_cols))

        return max_effort
