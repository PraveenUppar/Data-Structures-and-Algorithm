# You are given an integer array nums and an integer k, return true 
# if it is possible to divide this array into k non-empty subsets whose sums are all equal.


def parition(nums, k):

    if sum(nums) % k != 0:
        return False
    
    nums.sort(reverse = True)
    target = sum(nums) // k
    subset = [0] * k

    def backtracking(i):

        if i == len(nums):
            return True

        for j in range(k):
            if subset[j] + nums[i] <= target:
                subset[j] += nums[i]
                if backtracking(i + 1):
                    return True
                subset[j] -= nums[i] 
        return False

    return backtracking(0)
    