# You are given an integer n representing the number of steps to reach the top of a staircase. 
# You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.

memo = {}

def climb(n):

    def recursion(i):

        if i == n:
            return 1

        if i >= n:
            return 0

        if i in memo:
            return memo[i]

        res = recursion(i + 1) + recursion(i + 2)
        memo[i] = res
        return res


    return recursion(0)
    