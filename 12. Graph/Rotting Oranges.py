class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row = len(grid)
        cols = len(grid[0])
        visited = grid
        rotten = deque()
        fresh = 0
        mintues = 0

        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        if rotten is None:
            return -1 
        
        mintues = -1
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while rotten:
            size = len(rotten)
            while size > 0:
                x, y = rotten.popleft()
                size -= 1
                for dx, dy in dirs:
                    i = x + dx
                    j = y + dy
                    if 0 <= i < row and 0 <= j < cols and visited[i][j] == 1:
                        visited[i][j] = 2
                        fresh -= 1
                        rotten.append((i, j))
            mintues += 1
        

        if fresh == 0:
            return mintues
        return -1
