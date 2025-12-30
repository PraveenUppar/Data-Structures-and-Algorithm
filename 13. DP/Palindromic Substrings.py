class Solution:
    def countSubstrings(self, s: str) -> int:

        # Recursion
        # res = 0

        # for l in range(len(s)):
        #     for r in range(l, len(s)):
        #         while l < r and s[l] == s[r]:
        #             l += 1
        #             r -= 1
        #         if l >= r:
        #             res += 1
        # return res

        # Two pointers
        res = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

        