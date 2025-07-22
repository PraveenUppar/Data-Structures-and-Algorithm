from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
    
        # Get the total number of elements in the height list
        n = len(height)

        #Initialize two pointers: one at the beginning (left) and one at the end (right) of the list
        left = 0
        right = n - 1

        #  Variable to store the maximum area found
        max_area = 0

        # Use a while loop that continues until the two pointers meet
        while left < right:

            # Remember for width we use i-j for height we use height[i]-height[j]

            # Calculate the width between the two pointers
            w = right - left

            # Determine the height based on the shorter line between the two pointers
            h = min(height[left], height[right])

            # Calculate the area and update max_area if this area is larger
            area = w * h
            max_area = max(max_area, area)


            # Move the pointer pointing to the shorter line inward, trying to find a larger area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Test Cases
sol = Solution()

print(f"Input: [1,8,6,2,5,4,8,3,7], Output: {sol.maxArea([1,8,6,2,5,4,8,3,7])}")
print(f"Input: [1,1], Output: {sol.maxArea([1,1])}")
print(f"Input: [4,3,2,1,4], Output: {sol.maxArea([4,3,2,1,4])}")
print(f"Input: [1,2,1], Output: {sol.maxArea([1,2,1])}")
print(f"Input: [2,3,4,5,18,17,6], Output: {sol.maxArea([2,3,4,5,18,17,6])}")
print(f"Input: [0,0,0,0], Output: {sol.maxArea([0,0,0,0])}")
print(f"Input: [0,10,0], Output: {sol.maxArea([0,10,0])}")
