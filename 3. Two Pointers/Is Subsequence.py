class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

       # Get the length of both input strings s and t
        S = len(s)
        T = len(t)

        # If string s is empty, it is always a subsequence of any string, so return True
        if s == '':
            return True

        # If string s is longer than string t, it can't be a subsequence, so return False
        if S > T:
            return False

        # Initialize a pointer j to track the current index of string s
        j = 0

        # Iterate over each character in string t using index i
        for i in range(T):
            # If the current character in t matches the current character in s (s[j]),
            # check if we have matched the entire string s
            if t[i] == s[j]:
                # If we are at the last character of s, it means s is a subsequence of t
                if j == S - 1:
                    return True
                # Move to the next character in s by incrementing j
                j += 1

        # If the loop completes and we haven't returned True, s is not a subsequence of t
        return False



# Test Cases
sol = Solution()

print(f"s = 'abc', t = 'ahbgdc' -> {sol.isSubsequence('abc', 'ahbgdc')}")
print(f"s = 'axc', t = 'ahbgdc' -> {sol.isSubsequence('axc', 'ahbgdc')}")
print(f"s = '', t = 'ahbgdc' -> {sol.isSubsequence('', 'ahbgdc')}")
print(f"s = 'abc', t = '' -> {sol.isSubsequence('abc', '')}")
print(f"s = 'ace', t = 'abcde' -> {sol.isSubsequence('ace', 'abcde')}")
print(f"s = 'abc', t = 'abc' -> {sol.isSubsequence('abc', 'abc')}")
print(f"s = 'sing', t = 'sting' -> {sol.isSubsequence('sing', 'sting')}")
print(f"s = 'basic', t = 'abracadabra' -> {sol.isSubsequence('basic', 'abracadabra')}")
