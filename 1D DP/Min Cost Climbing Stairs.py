# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. 
# After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

# You may choose to start at the index 0 or the index 1 floor.

# Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

def climb(cost):

    memo = {}

    def recursion(i):

        if i > len(cost):
            return 0 

        if i in memo:
            return memo[i]

        res = cost[i] + min(recursion(i + 1), recursion(i + 2))
        memo[i] = res
        return res


    return recursion(0)