# You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

# Return true if you can reach the last index starting from index 0, or false otherwise.

def jump(nums):

    memo = {}

    def solve(i):
        if i >= len(nums) - 1:
            return True 

        if i in memo:
            return memo[i]

        for j in range(1, len(nums + 1)):
            if solve(i + j):
                memo[i] = True
                return True 

        memo[i] = False
        return False

    return solve(0)