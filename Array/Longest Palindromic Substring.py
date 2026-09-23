# Given a string s, return the longest substring of s that is a palindrome.

# A palindrome is a string that reads the same forward and backward.

# If there are multiple palindromic substrings that have the same length, return any one of them.

def palindrome(s):

    longest = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i: i + j]
            if substring == substring[::-1]:
                if len(substring) > longest:
                    longest = substring
    return longest