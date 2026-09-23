# Given two strings text1 and text2, return the length of the longest common subsequence between the two strings 
# if one exists, otherwise return 0.

# A subsequence is a sequence that can be derived from the given sequence by deleting some or 
# no elements without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".
# A common subsequence of two strings is a subsequence that exists in both strings.

def longest(s1, s2):

    memo = {}

    def recursion(i, j):

        if i == len(s1) and j == len(s2):
            return 0 

        if (i,j) in memo:
            return memo[(i,j)]

        if s1[i] == s2[j]:
            return 1 + recursion(i + 1, j + 1)

        res = max(recursion(i + 1, j), recursion(i, j + 1))
        memo[(i,j)] = res
        return res 

    recursion(0,0)

