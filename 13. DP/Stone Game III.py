class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)
        dp= [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            curr_sum = 0
            dp[i] = float("-inf")
            for k in range(3):
                if i + k < n:
                    curr_sum += stoneValue[i + k]
                    score = curr_sum - dp[i + k + 1]
                    dp[i] = max(dp[i], score)
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
                