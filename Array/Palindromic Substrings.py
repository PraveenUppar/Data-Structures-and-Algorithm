# Given a string s, return the number of substrings within s that are palindromes.

# A palindrome is a string that reads the same forward and backward.

def palindrome(s):

    count = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i: i + j]
            if substring == substring[::-1]:
                count += 1
    return count