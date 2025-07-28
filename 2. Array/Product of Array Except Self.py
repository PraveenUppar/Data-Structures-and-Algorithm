from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = 1
        suff[n - 1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i] 
        return res

# Test Cases
sol = Solution()

print(f"Input: [1,2,3,4], Output: {sol.productExceptSelf([1,2,3,4])}")
print(f"Input: [-1,1,0,-3,3], Output: {sol.productExceptSelf([-1,1,0,-3,3])}")
print(f"Input: [0,0], Output: {sol.productExceptSelf([0,0])}")
print(f"Input: [5], Output: {sol.productExceptSelf([5])}")
# Expected: [1] (or [1] depending on problem constraints for single element)
# Note: LeetCode problem statement implies n >= 2, but a single element test is good for robustness.
# If n=1, the product of elements *except* self would technically be 1.
print(f"Input: [2,3], Output: {sol.productExceptSelf([2,3])}")


# BRUTE FORCE SOLUTION 

#         ans = []
#         for i in range(len((nums))):
#             ans_sum = 1
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 else:
#                     ans_sum *= nums[j]
#             ans.append(ans_sum)
#         return ans
