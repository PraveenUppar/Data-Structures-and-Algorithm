# You are given an array of integers nums and an integer target.

# For each number in the array, you can choose to either add or subtract it to a total sum.

# For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
# If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

# Return the number of different ways that you can build the expression such that the total sum equals target.


def solve(nums, target):

    memo = {}

    def recursion(i, total):

        if i == len(nums):
            if total == target:
                return 1
            else:
                return 0 

        if (i, total) in memo:
            return memo[(i, total)]

        add = recursion(i + 1, total + nums[i])
        sub = recursion(i + 1, total - nums[i])

        res = add + sub 
        memo[(i, total)] = res 
        return res

    return recursion(0, 0)