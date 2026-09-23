# You are given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

def combinations(n, k):

    nums = []

    for i in range(1, n):
        nums.append(i)

    res = []
    
    def backtracking(i, subset):

        if i == k:
            res.append(subset.copy())
            return 

        subset.append(nums[i])
        backtracking(i + 1, subset)
        
        subset.pop()
        backtracking(i + 1, subset)

    backtracking(0, [])
    return res