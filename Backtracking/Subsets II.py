# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

# The solution must not contain duplicate subsets. You may return the solution in any order.

def subsets(nums):

    res = set()

    def backtracking(i, subset):

        if i == len(nums):
            res.add(tuple(subset.copy()))
            return 

        subset.append(nums[i])
        backtracking(i + 1, subset)
        
        subset.pop()
        backtracking(i + 1, subset)

    backtracking(0, [])
    return list(res)
