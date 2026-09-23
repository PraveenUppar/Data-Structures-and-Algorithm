# A company has limited resources, it can only finish at most k distinct projects before the IPO. 
# Help the company to design the best way to maximize its total capital after finishing at most k distinct projects.

# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it. 
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

# The answer is guaranteed to fit in a 32-bit signed integer.

import heapq

def ipo(k, w, profit, capital):
    max_profit = []
    min_capital = []

    for i in range(len(capital)):
        pair = (capital[i], profit[i])
        min_capital.append(pair)

    heapq.heapify(min_capital)

    for _ in range(k):
        while min_capital and min_capital[0][0] <= w:
            c, p = heapq.heappop(min_capital)
            heapq.heappush(max_profit, -p)

        if not max_profit:
            break

        w += heapq.heappop(max_profit)

    return w