from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums
        
# Test Cases
sol = Solution()

# Test Case 1
nums1 = [0,1,0,3,12]
sol.moveZeroes(nums1)
print(f"Input: [0,1,0,3,12], Output: {nums1}")

# Test Case 2
nums2 = [0]
sol.moveZeroes(nums2)
print(f"Input: [0], Output: {nums2}")

# Test Case 3
nums3 = [1,0]
sol.moveZeroes(nums3)
print(f"Input: [1,0], Output: {nums3}")

# Test Case 4
nums4 = [1,2,3]
sol.moveZeroes(nums4)
print(f"Input: [1,2,3], Output: {nums4}")

# Test Case 5
nums5 = [0,0,0,1,0,2,0,3]
sol.moveZeroes(nums5)
print(f"Input: [0,0,0,1,0,2,0,3], Output: {nums5}")

# Test Case 6
nums6 = []
sol.moveZeroes(nums6)
print(f"Input: [], Output: {nums6}")

# Test Case 7
nums7 = [0,0,0,0,0]
sol.moveZeroes(nums7) 
print(f"Input: [0,0,0,0,0], Output: {nums7}")
