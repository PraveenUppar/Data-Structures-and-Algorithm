from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        profit = 0
        total_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                total_profit += profit
                buy = prices[i]
        return total_profit
        