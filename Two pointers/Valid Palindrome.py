# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.


def palindrom(s):
    newStr = ''
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]
