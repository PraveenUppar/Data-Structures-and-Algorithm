# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.

def valid(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    return sorted_s == sorted_t