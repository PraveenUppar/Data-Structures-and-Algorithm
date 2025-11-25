class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = []

        for _ in range(n):
            row = ["."] * n
            board.append(row)
        
        col = [False] * n               # column size of the board
        diag1 = [False] * (2 * n - 1)   # diag1 size of the board
        diag2 = [False] * (2 * n - 1)   # diag2 size of the board

        def backtrack(row):
            if row == n:
                for r in board:
                    result.append(["".join(r)])
                return 

            for c in range(n):
                d1 = row - c + n - 1  # indexing for main diagonal
                d2 = row + c          # indexing for other diagonal
                if not col[c] and not diag1[d1] and not diag2[d2]:
                    col[c] = diag1[d1] = diag2[d2] = True
                    board[row][c] = "Q"

                    backtrack(row + 1)

                    board[row][c] = "."
                    col[c] = diag1[d1] = diag2[d2] = False
        backtrack(0)
        return result
        