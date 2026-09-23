# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) 
# and an integer amount representing a target amount of money.

# Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

# You may assume that you have an unlimited number of each coin and that each value in coins is unique.

def change(coins, amount):

    memo = {}

    def recursion(i, target):

        if target == 0:
            return 1

        if i == len(coins) or target < 0:
            return 0

        if (i, target) in memo:
            return memo[(i, target)]

        res = 0

        if target > coins[i]:
            res = recursion(i + 1, target)
            res += recursion(i, target - coins[i])

        memo[(i, target)] = res 
        return res 
    
    recursion(0 , amount)