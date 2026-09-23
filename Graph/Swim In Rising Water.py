# You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).

# Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.

# You may swim either horizontally or vertically in the grid between two adjacent squares 
# if the original elevation of both squares is less than or equal to the water level at time t.

# Starting from the top left square (0, 0), 
# return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).

import heapq

def swim(grid):
    n = len(grid)
    min_heap = [[grid[0][0], 0, 0]]
    visited = set()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while min_heap:
        time, curr_row, curr_col = heapq.heappop(min_heap)

        if (curr_row, curr_col) in visited:
            continue

        visited.add((curr_row, curr_col))

        if (curr_row, curr_col) == (n - 1, n - 1):
            return time

        for dr, dc in directions:
            nei_row = curr_row + dr
            nei_col = curr_col + dc

            if 0 <= nei_row < n and 0 <= nei_col < n and (nei_row, nei_col) not in visited:
                new_time = max(time, grid[nei_row][nei_col])
                heapq.heappush(min_heap, [new_time, nei_row, nei_col])

    return -1   