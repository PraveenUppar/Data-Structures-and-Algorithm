class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Brute Force - TLE
        # max_count = 0

        # for i in range(len(s)):
        #     count = 1
        #     change = 0
        #     for j in range(i+1,len(s)):
        #         if s[i] == s[j]:
        #             count += 1
        #         if s[i] != s[j] and change < k:
        #             count += 1
        #             change += 1
        #     max_count = max(count,max_count)
        # return max_count 