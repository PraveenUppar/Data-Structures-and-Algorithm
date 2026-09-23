# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. 
# Suppose the stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the smallest possible weight of the left stone. If there are no stones left, return 0


def laststone(stones):

    stonesum = sum(stones)
    memo = {}

    def recursion(i ,total):

        if i == len(stones):
            return abs(total - (stonesum - total))

        if (i, total) in memo:
            return memo[(i, total)]

        skip = recursion(i + 1, total)
        include = recursion(i + 1, total + stones[i])

        res = min(skip, include)
        memo[(i,total)] = res
        return res 

    recursion(0,0)