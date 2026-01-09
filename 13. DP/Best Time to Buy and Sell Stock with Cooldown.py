class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Recursion using dfs

        # def dfs(i, buying):

        #     if i >= len(prices):
        #         return 0
            
        #     cooldown = dfs(i + 1,buying)
        #     if buying:
        #         buying = dfs(i + 1, not buying) - prices[i]
        #         return max(buying,cooldown)
        #     else:
        #         selling = dfs(i + 2, not buying) + prices[i]
        #         return max(selling,cooldown)

        # return dfs(0, True)

        # Top down DP

        dp = {}  

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

        # hold = -prices[0]
        # sold = 0
        # cool = 0

        # for i in range(1 , len(prices)):
        #     curr_hold = max(hold, cool - prices[i])
        #     curr_sold = hold + prices[i]
        #     curr_cool = max(cool, sold)
        #     hold, sold, cool = curr_hold, curr_sold, curr_cool

        # return max(sold,cool)

        
        