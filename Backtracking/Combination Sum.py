# You are given an array of distinct integers nums and a target integer target. 
# Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

# The same number may be chosen from nums an unlimited number of times. 
# Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

def combination_sum(nums, target):

    res = []

    def backtracking(i, curr_sum, subset):

        if curr_sum == target:
            res.append(subset.copy())
            return 

        if i == len(nums) or curr_sum > target:
            return

        subset.append(nums[i])
        backtracking(i + 1, curr_sum + nums[i], subset)
        
        subset.pop()
        backtracking(i + 1 ,curr_sum, subset)
        
    backtracking(0, 0, [])
    return res


