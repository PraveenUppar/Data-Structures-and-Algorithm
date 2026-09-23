# You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. 
# For example, if you are at nums[i], you can jump to any index i + j where:

# j <= nums[i]
# i + j < nums.length
# You are initially positioned at nums[0].

# Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). 
# You may assume there is always a valid answer.

def jump(nums):

    memo = {}

    def solve(i):
        if i >= len(nums) - 1:
            return 0

        if nums[i] == 0:
            return float('inf') 

        if i in memo:
            return memo[i]

        min_jumps = float('inf')

        for j in range(1, len(nums + 1)):
            res = solve(i + j)
            if res != float("inf"):
                min_jumps = min(min_jumps, res + 1)
             
        memo[i] = min_jumps
        return min_jumps

    return solve(0)