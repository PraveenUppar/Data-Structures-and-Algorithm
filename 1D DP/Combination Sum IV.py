# You are given an array of distinct integers nums and a target integer target, 
# return the number of possible combinations that add up to target.

def combinations(nums, target):

    memo = {}
    nums.sort()

    def recursion(amount):

        if amount == 0:
            return 1

        if amount in memo:
            return memo[amount]

        res = 0

        for num in nums:
            if amount - num <= target:
                res += recursion(amount - num)

        memo[target] = res
        return res

    return recursion(target)