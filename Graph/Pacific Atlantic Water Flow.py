# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. 
# Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. 
# Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. 
# You may return the answer in any order.

def ocean(heights):

    row = len(heights)
    cols = len(heights[0])
    pacific = set()
    atlantic = set()

    def waterflow(r,c,visited,prev_height):

        if r < 0 or c < 0 or r >= row or c >= cols or (r,c) in visited or heights[r][c] < prev_height:
            return

        visited.add((r,c))

        waterflow(r + 1, c, visited, heights[r][c])
        waterflow(r - 1, c, visited, heights[r][c])
        waterflow(r, c + 1, visited, heights[r][c])
        waterflow(r, c - 1, visited, heights[r][c])


    for c in range(cols):
        waterflow(0,c,pacific, heights[0][c])

    for r in range(row):
        waterflow(r,0,pacific, heights[r][0])

    for c in range(cols):
        waterflow(row - 1,c,atlantic, heights[row - 1][c])

    for r in range(row):
        waterflow(r,cols - 1,atlantic, heights[r][cols - 1])

    return list(pacific & atlantic)


