# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

# You may return the solution in any order.

def partition(s):

    res = []

    def palindrome(string):
        return string == string[::-1]

    def backtracking(i, subset):

        if i == len(s):
            res.append(subset.copy())
            return

        for j in range(i, len(s)):
            string = s[i: j + 1]
            if palindrome(string):
                subset.append(string)
                backtracking(j + 1, subset)
                subset.pop()

    backtracking(0, [])
    return res