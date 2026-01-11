class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        dp = {}

        def dfs(l,r):

            if l > r:
                return 0
                
            if (l, r) in dp:
                return dp[(l, r)]

            alice_turn = (r - l) % 2 == 0

            if alice_turn:
                left = piles[l]
                right = piles[r]
            else:
                left = 0
                right = 0

            dp[(l,r)] = max(dfs(l + 1, r) + left, dfs(l, r- 1) + right)
            return dp[(l,r)]

        total_sum = sum(piles)
        alice_score = dfs(0, len(piles) - 1)
        bob_score = total_sum - alice_score

        if alice_score > bob_score:
            return True
        else:
            return False        