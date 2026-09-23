# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

def generate(n):

    res = []

    def backtracking(open, close, s):

        if open == close and open + close == n * 2:
            res.append(s)
            return 

        if open < n:
            backtracking(open + 1, close, s + "(")

        if close < open:
            backtracking(open, close + 1, s + ")")

    backtracking(0, 0, "")
    return res