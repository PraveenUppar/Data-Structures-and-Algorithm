# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. However, you can buy it then immediately sell it on the same day. 
# Also, you are allowed to perform any number of transactions but can hold at most one share of the stock at any time.

# Find and return the maximum profit you can achieve.

def stocks(prices):
    buy = prices[0]
    profit = 0
    total = 0

    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]

        else:
            profit = prices[i] - buy
            total += profit
            buy = prices[i]

    return total