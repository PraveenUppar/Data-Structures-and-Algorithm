# You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.

# A palindrome is a string that reads the same forward and backward.

def palindrome(s):
    return s == s[::-1]