from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        # Initialize prefix and suffix arrays
        prefix_products = [1] * n
        suffix_products = [1] * n
        
        # Calculate prefix products
        # prefix_products[i] will contain the product of all elements to the left of i
        # For index 0, there are no elements to the left, so it's 1
        for i in range(1, n):
            prefix_products[i] = prefix_products[i-1] * nums[i-1]
            
        # Calculate suffix products
        # suffix_products[i] will contain the product of all elements to the right of i
        # For the last index (n-1), there are no elements to the right, so it's 1
        for i in range(n - 2, -1, -1): # Iterate from n-2 down to 0
            suffix_products[i] = suffix_products[i+1] * nums[i+1]
            
        # Calculate the final answer
        answer = [0] * n
        for i in range(n):
            answer[i] = prefix_products[i] * suffix_products[i]
            
        return answer

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
