# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) 
# and an integer amount representing a target amount of money.

# Return the fewest number of coins that you need to make up the exact target amount. 
# If it is impossible to make up the amount, return -1.

# You may assume that you have an unlimited number of each coin.

def change(coins, target):

    memo = {}

    def recursion(amount):

        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        res = float("inf")

        for coin in coins:
            if amount - coin <= target:
                res = min(res, 1 + recursion(amount - coin))

        memo[amount] = res
        return res
    
    min_coins = recursion(target)

    if min_coins == float("inf"):
        return -1
    else:
        return min_coins