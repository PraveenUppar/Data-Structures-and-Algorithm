# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

def oranges(grid):

    row = len(grid)
    cols = len(grid[0])
    fresh = 0
    time = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for r in range(row):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1

    while fresh:
        flag = False 
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 2:
                    for dr, dc in directions:
                        new_r = r + dr
                        new_c = c + dc
                        if 0 <= new_r < r and 0 <= new_c < 0 and grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 3
                            fresh -= 1
                            flag = True

        if not flag:
            return - 1

        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 3:
                    grid[r][c] = 2

        time += 1

    return time