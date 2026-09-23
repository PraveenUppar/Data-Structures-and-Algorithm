# Given an array nums of unique integers, return all possible subsets of nums.
# The solution set must not contain duplicate subsets. You may return the solution in any order.

def subsets(nums):

    res = []

    def backtracking(i, subset):

        if i == len(nums):
            res.append(subset.copy())
            return 

        subset.append(nums[i])
        backtracking(i + 1, subset)
        
        subset.pop()
        backtracking(i + 1, subset)

    backtracking(0, [])
    return res
