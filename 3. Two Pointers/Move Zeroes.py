from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = 0  # Pointer for the position where the next non-zero element should be placed

        # Iterate through the array with 'i'
        # If nums[i] is non-zero, swap it with the element at non_zero_idx
        # and then increment non_zero_idx
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_idx], nums[i] = nums[i], nums[non_zero_idx]
                non_zero_idx += 1
        
# Test Cases
sol = Solution()

# Test Case 1
nums1 = [0,1,0,3,12]
sol.moveZeroes(nums1)
print(f"Input: [0,1,0,3,12], Output: {nums1}")
# Expected: [1,3,12,0,0]

# Test Case 2
nums2 = [0]
sol.moveZeroes(nums2)
print(f"Input: [0], Output: {nums2}")
# Expected: [0]

# Test Case 3
nums3 = [1,0]
sol.moveZeroes(nums3)
print(f"Input: [1,0], Output: {nums3}")
# Expected: [1,0]

# Test Case 4
nums4 = [1,2,3]
sol.moveZeroes(nums4)
print(f"Input: [1,2,3], Output: {nums4}")
# Expected: [1,2,3]

# Test Case 5
nums5 = [0,0,0,1,0,2,0,3]
sol.moveZeroes(nums5)
print(f"Input: [0,0,0,1,0,2,0,3], Output: {nums5}")
# Expected: [1,2,3,0,0,0,0,0]

# Test Case 6
nums6 = []
sol.moveZeroes(nums6)
print(f"Input: [], Output: {nums6}")
# Expected: []

# Test Case 7
nums7 = [0,0,0,0,0]
sol.moveZeroes(nums7)
print(f"Input: [0,0,0,0,0], Output: {nums7}")
# Expected: [0,0,0,0,0]