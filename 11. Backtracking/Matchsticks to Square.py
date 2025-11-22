class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks) % 4 != 0:
            return False
        
        sides = [0] * 4
        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)

        def dfs(index):
            if index == len(matchsticks):
                return True

            for i in range(4):
                if sides[i] + matchsticks[index] <= target:
                    sides[i] += matchsticks[index]
                    if dfs(index+1):
                        return True
                    sides[i] -= matchsticks[index] 
            return False

        return dfs(0)
        