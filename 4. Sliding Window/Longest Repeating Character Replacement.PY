class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        left = 0
        max_freq = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_freq = max(max_freq, count[s[right]])
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest

        # Brute Force
        # longest = 0

        # for i in range(len(s)):
        #     count = {}
        #     max_freq = 0
        #     for j in range(i, len(s)):
        #         count[s[j]] = 1 + count.get(s[j], 0)
        #         max_freq = max(max_freq, count[s[j]])
        #         if (j - i + 1) - max_freq <= k:
        #             longest = max(longest, j - i + 1)
        # return longest