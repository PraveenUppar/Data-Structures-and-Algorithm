class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

# dividing the stones into two subsets (Group A and Group B) such that the difference between their sums is minimized
        
        # Recursion using dfs
        # stoneSum = sum(stones)
        # targetSum = stoneSum + 1 // 2

        # def dfs(i, total):
        #     if i == len(stones) or total >= targetSum:
        #         return abs(total - (stoneSum - total))
        #     else:
        #         return min(dfs(i + 1,total), dfs(i + 1, total + stones[i]))
        # return dfs(0,0)

        # Top down DP
        stoneSum = sum(stones)
        targetSum = stoneSum + 1 // 2
        dp = {}

        def dfs(i, total):
            if i == len(stones) or total >= targetSum:
                return abs(total - (stoneSum - total))

            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(dfs(i + 1,total), dfs(i + 1, total + stones[i]))
            return dp[(i, total)]

        return dfs(0,0)


        
        