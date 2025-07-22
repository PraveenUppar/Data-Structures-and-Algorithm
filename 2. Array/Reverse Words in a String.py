class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()  # Splits by whitespace and handles multiple spaces
        words.reverse()    # Reverses the list of words
        return " ".join(words) # Joins them back with a single space
    
        # words = s.split()
        # left, right = 0, len(words) - 1

        # while left < right:
        #     words[left], words[right] = words[right], words[left]
        #     left += 1
        #     right -= 1

        # return " ".join(words) 

# Test Cases
sol = Solution()
print(f"Input: 'the sky is blue', Output: '{sol.reverseWords('the sky is blue')}'")
print(f"Input: '  hello world  ', Output: '{sol.reverseWords('  hello world  ')}'")
print(f"Input: 'a good   example', Output: '{sol.reverseWords('a good   example')}'")
print(f"Input: ' ', Output: '{sol.reverseWords(' ')}'")
print(f"Input: 'singleword', Output: '{sol.reverseWords('singleword')}'")
print(f"Input: '   leading and trailing   spaces   ', Output: '{sol.reverseWords('   leading and trailing   spaces   ')}'")