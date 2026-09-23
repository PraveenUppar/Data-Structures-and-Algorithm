# Given a string s, return all possible ways to partition it into a list of substrings, 
# such that every possible substring in every possible partition is covered.

def parition(s):

    res = []

    def backtracking(i, subset):

        if i == len(s):
            res.append(subset.copy())
            return

        for j in range(i, len(s)):
            string = s[i : j + 1]
            subset.append(string)
            backtracking(j + 1, subset)
            subset.pop()

    backtracking(0, [])
    return res
