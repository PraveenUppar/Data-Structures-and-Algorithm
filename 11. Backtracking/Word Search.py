class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        L = len(word)

        if L > m * n:
            return False

        def dfs(i, j ,index):
            # base case
            if index == L:
                return True
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] != word[index]:
                return False
            
            tmp = board[i][j]
            board[i][j] = "#"

            found = (dfs(i+1, j, index + 1) or dfs(i-1, j, index + 1) or dfs(i, j+1, index + 1) or dfs(i, j-1, index + 1))
            board[i][j] == tmp
            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False



        