class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i,j,visted):
            visted.add((i,j))
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if 0 <= x < row and 0 <= y < cols:
                    if (x, y) in visted:
                        continue
                    if heights[x][y] >= heights[i][j]:
                        dfs(x, y, visted)

        for c in range(cols):
            dfs(0, c, pacific)         
            dfs(row - 1, c, atlantic)  

        for r in range(row):
            dfs(r, 0, pacific)          
            dfs(r, cols - 1, atlantic)

        return list(pacific & atlantic)
        