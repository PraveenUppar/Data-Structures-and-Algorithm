# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.

# Return the weight of the last remaining stone or return 0 if none remain.

import heapq

def laststone(stones):

    stone_weight = []

    for i in range(len(stones)):
        stone_weight.append(-stones[i])

    heapq.heapify(stone_weight)

    while len(stone_weight) > 1:

        stone1 = heapq.heappop(stone_weight)
        stone2 = heapq.heappop(stone_weight)

        if stone1 != stone2:
            new_stone = abs(stone2 - stone1)
            heapq.heappush(stone_weight, -new_stone)
        
    stone_weight.append(0)
    return abs(stone_weight[0])
