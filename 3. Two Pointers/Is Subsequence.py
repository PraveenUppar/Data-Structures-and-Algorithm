class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 # Pointer for string s
        j = 0 # Pointer for string t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1 # Move s pointer only if characters match
            j += 1     # Always move t pointer

        # If i reaches the end of s, it means all characters of s were found in t in order
        return i == len(s)

# Test Cases
sol = Solution()

print(f"s = 'abc', t = 'ahbgdc' -> {sol.isSubsequence('abc', 'ahbgdc')}")
# Expected: True

print(f"s = 'axc', t = 'ahbgdc' -> {sol.isSubsequence('axc', 'ahbgdc')}")
# Expected: False

print(f"s = '', t = 'ahbgdc' -> {sol.isSubsequence('', 'ahbgdc')}")
# Expected: True (empty string is always a subsequence)

print(f"s = 'abc', t = '' -> {sol.isSubsequence('abc', '')}")
# Expected: False

print(f"s = 'ace', t = 'abcde' -> {sol.isSubsequence('ace', 'abcde')}")
# Expected: True

print(f"s = 'abc', t = 'abc' -> {sol.isSubsequence('abc', 'abc')}")
# Expected: True

print(f"s = 'sing', t = 'sting' -> {sol.isSubsequence('sing', 'sting')}")
# Expected: True

print(f"s = 'basic', t = 'abracadabra' -> {sol.isSubsequence('basic', 'abracadabra')}")
# Expected: False