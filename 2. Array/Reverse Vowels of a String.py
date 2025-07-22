class Solution:
    def reverseVowels(self, s: str) -> str:

        # We cannot work with strigs directly we need to convert it to list to perform opertaions
        s_list = list(s)
        vowels = "aeiouAEIOU"
        
        left = 0
        right = len(s_list) - 1
        
        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            if left < right:
                # Exchange the strings
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return "".join(s_list)

sol = Solution()

print(f"Input: 'hello', Output: '{sol.reverseVowels('hello')}'")
print(f"Input: 'leetcode', Output: '{sol.reverseVowels('leetcode')}'")
print(f"Input: 'aA', Output: '{sol.reverseVowels('aA')}'")
print(f"Input: 'race car', Output: '{sol.reverseVowels('race car')}'")
print(f"Input: 'bcdfgh', Output: '{sol.reverseVowels('bcdfgh')}'")
print(f"Input: '', Output: '{sol.reverseVowels('')}'")
print(f"Input: 'aeiou', Output: '{sol.reverseVowels('aeiou')}'")