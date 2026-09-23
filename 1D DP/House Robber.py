# You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
# The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses 
# because the security system will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.


def house(nums):

    memo = {}

    def reucursion(i):

        if i >= len(nums):
            return 0

        if i in memo:
            return memo[i]

        rob = nums[i] + reucursion(i + 1)
        skip = reucursion(i + 1)

        res = max(rob, skip)
        memo[i] = res
        return res

    reucursion(0)