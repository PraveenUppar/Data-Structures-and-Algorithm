from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit



        # Not worked for all test cases

        # nums = prices
        # smallest = 0
        # diff = 0
        # max_diff = 0

        # for i in range(len(nums)):
        #     if nums[i] < nums[i-1]:
        #         smallest = i
        #         for j in range(smallest,len(nums)):
        #             if nums[smallest] < nums[j]:
        #                 diff = nums[j] - nums[smallest]
        #                 max_diff = max(diff,max_diff)

        # if max_diff == 0:
        #     return 0

        # max(diff,max_diff)
        # return max_diff



        