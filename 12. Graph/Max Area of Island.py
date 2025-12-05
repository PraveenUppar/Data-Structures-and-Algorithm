class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r == row or c == cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    res = max(res, dfs(r, c))
        return res
        