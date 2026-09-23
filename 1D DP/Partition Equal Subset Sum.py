# You are given an array of positive integers nums.

# Return true if you can partition the array into two subsets, subset1 and subset2 
# where sum(subset1) == sum(subset2). Otherwise, return false.

def partition(nums):

    if sum(nums) % 2 != 0:
        return False 

    target = sum(nums) // 2

    memo = {}

    def recursion(i, amount):

        if amount == 0:
            return True

        if amount < 0 or i >= len(nums):
            return False

        if(i, amount) in memo:
            return memo[i]

        exclude = recursion(i + 1, amount)
        include = recursion(i + 1, amount - nums[i])

        res = exclude or include
        memo[(i, target)] = res
        return res


    recursion(0, target)