class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.count = 0
        
        col = [False] * n               
        diag1 = [False] * (2 * n - 1)   
        diag2 = [False] * (2 * n - 1)   

        def backtrack(row):
            if row == n:
                self.count += 1 
                return 

            for c in range(n):
                d1 = row - c + n - 1 
                d2 = row + c          
                
                if not col[c] and not diag1[d1] and not diag2[d2]:
                    col[c] = diag1[d1] = diag2[d2] = True
                    backtrack(row + 1)
                    col[c] = diag1[d1] = diag2[d2] = False

        backtrack(0)
        return self.count