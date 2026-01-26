class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        left = 0
        curr = set()

        for right in range(len(s)):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            curr.add(s[right])
            longest = max(longest, len(curr))
        return longest

        # Works but slow
        # longest = 0

        # for i in range(len(s)):
        #     curr = set()
        #     for j in range(i, len(s)):
        #         if s[j] in curr:
        #             break
        #         curr.add(s[j])
        #         longest = max(longest, len(curr))
        # return longest

        
         
