class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        subarray_char = set()
        count = 0
        left = 0

        for right in range(len(s)):
            while s[right] in subarray_char:
                subarray_char.remove(s[left])
                s += 1
            subarray_char.add(s[right])
            count = max(count,right-left+1)
        return count

        # Brute Force - TLE O(n∗m)
        # count = 0

        # for i in range(len(s)):
        #     subarray_char = set()
        #     for j in range(i,len(s)):
        #         if s[j] in subarray_char:
        #             break
        #         subarray_char.add(s[j])
        #     count = max(count,len(subarray_char))
        # return count        