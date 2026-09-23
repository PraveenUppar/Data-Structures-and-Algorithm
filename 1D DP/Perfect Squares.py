# You are given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer. For example, 1, 4, 9, 16, 25... are perfect squares.

def perfect(n):

    memo = {}

    def recursion(amount):

        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        res = float('inf')

        for i in range(1,amount):
            if i * i <= amount:
                res = min(res, 1 + recursion(amount - (i * i)))
            

        memo[amount] = res
        return res

    return recursion(n)