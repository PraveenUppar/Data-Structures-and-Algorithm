class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
            dictionary_set = set(dictionary)

            def dp(i):
                if i == len(s):
                    return 0
                ans = dp(i + 1) + 1
                for j in range(i , len(s)):
                    curr = s[i:j + 1]
                    if curr in dictionary_set:
                        ans = min(ans, dp(j + 1))
                return ans

            return dp(0)