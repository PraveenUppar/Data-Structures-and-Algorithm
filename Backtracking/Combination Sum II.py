# You are given an array of integers candidates, which may contain duplicates, and a target integer target. 
# Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

# Each element from candidates may be chosen at most once within a combination. 
# The solution set must not contain duplicate combinations.

# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

def combination_sum(nums, target):

    res = set()

    def backtracking(i, curr_sum, subset):

        if curr_sum == target:
            res.add(tuple(subset.copy()))
            return 

        if i == len(nums) or curr_sum > target:
            return

        subset.append(nums[i])
        backtracking(i + 1, curr_sum + nums[i], subset)

        subset.pop()
        backtracking(i + 1 ,curr_sum, subset)
        
    backtracking(0, 0, [])
    return list(res)