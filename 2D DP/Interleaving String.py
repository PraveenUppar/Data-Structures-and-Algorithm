# You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

# Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met

# |n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...
# You may assume that s1, s2 and s3 consist of lowercase English letters.

def isInterleave(s1,s2,s3):

    if len(s1) + len(s2) != len(s3):
        return False

    memo = {}

    def recursion(i, j, k):

        if k == len(s3):
            if i == len(s1) and j == len(s2):
                return True
        
        if (i, j) in memo:
            return memo[(i, j)]

        if i < len(s1) and s1[i] == s3[k]:
            if recursion(i + 1, j, k + 1):
                memo[(i, j)] = True
                return True

        if j < len(s2) and s2[j] == s3[k]:
            if recursion(i, j + 1, k + 1):
                memo[(i, j)] = True
                return True

        memo[(i, j)] = False
        return False

    return recursion(0, 0, 0)