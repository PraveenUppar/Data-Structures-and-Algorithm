class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        cols = len(board[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r == row or c == cols or board[r][c] == "X":
                return 
            
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(row):
            # check left boarder
            if board[r][0] == "O":
                dfs(r,0)
            # check right boarder
            if board[r][cols - 1] == "O":
                dfs(r,cols-1)
        
        for c in range(cols):
            # check top boarder
            if board[0][c] == "O":
                dfs(0,c)
            # check bottom boarder
            if board[row - 1][c] == "O":
                dfs(row - 1,c)

        # Replace
        for r in range(row):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"