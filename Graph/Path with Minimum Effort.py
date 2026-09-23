# You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). 
# You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). 
# You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

import heapq

def path(heights):

    row = len(heights)
    cols = len(heights[0])
    max_effort = 0

    min_heap = [[0,0,0]]
    visited = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while min_heap:

        effort, curr_row, curr_cols = heapq.heappop(min_heap)
        max_effort = max(max_effort, effort)

        if (curr_row, curr_cols) == (row - 1, cols - 1):
            return max_effort

        visited.add((curr_row, curr_cols))

        for dr, dc in directions:
            nei_row = curr_row + dr
            nei_col = curr_cols + dc 

            if 0 <= nei_row < row and 0 <= nei_col < cols and (nei_row, nei_col) not in visited:
                new_effort = max(effort, abs(heights[nei_row][nei_col] - heights[curr_row][curr_cols]))
                heapq.heappush(min_heap, [new_effort, nei_row, nei_col])

    return -1