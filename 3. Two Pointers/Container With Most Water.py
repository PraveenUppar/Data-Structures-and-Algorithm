from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the current width
            width = right - left
            
            # The height of the water is limited by the shorter line
            min_height = min(height[left], height[right])
            
            # Calculate current area
            current_area = min_height * width
            
            # Update max_area if current_area is greater
            max_area = max(max_area, current_area)
            
            # Move the pointer of the shorter line inwards
            # This is because moving the taller line will always result in a smaller or equal height
            # (limited by the shorter line) and a smaller width, thus a potentially smaller area.
            # Moving the shorter line gives a chance to find a taller line to potentially increase height.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

# Test Cases
sol = Solution()

print(f"Input: [1,8,6,2,5,4,8,3,7], Output: {sol.maxArea([1,8,6,2,5,4,8,3,7])}")
# Expected: 49 (Area formed by height[1]=8 and height[8]=7, width=7)

print(f"Input: [1,1], Output: {sol.maxArea([1,1])}")
# Expected: 1 (Area formed by height[0]=1 and height[1]=1, width=1)

print(f"Input: [4,3,2,1,4], Output: {sol.maxArea([4,3,2,1,4])}")
# Expected: 16 (Area formed by height[0]=4 and height[4]=4, width=4)

print(f"Input: [1,2,1], Output: {sol.maxArea([1,2,1])}")
# Expected: 2 (Area formed by height[1]=2 and either height[0] or height[2], width=1)

print(f"Input: [2,3,4,5,18,17,6], Output: {sol.maxArea([2,3,4,5,18,17,6])}")
# Expected: 17 (Area formed by height[4]=18 and height[5]=17, width=1 OR height[0]=2 and height[6]=6, width=6 gives 12, etc.)
# Specifically, 17 * 1 = 17, but for [2,3,4,5,18,17,6] it should be 17 * (5-4) = 17, no
# It would be min(height[4],height[5]) * (5-4) = min(18,17) * 1 = 17.
# Or consider (2,6) -> min(2,6) * (6-0) = 2 * 6 = 12.
# The expected 17 seems to align with the pair (18, 17) which are next to each other.
# For (2, 17), width is 5, min height is 2, area is 10.
# The actual max area here is between 18 and 6: min(18,6) * (6-4) = 6 * 2 = 12.
# Between 5 and 17: min(5,17) * (5-3) = 5 * 2 = 10.
# The actual max is 17. This example is tricky. Let's trace it.
# (2,6) -> min(2,6)*6 = 12, right moves. (2,17) -> min(2,17)*5 = 10, right moves.
# (2,18) -> min(2,18)*4 = 8, right moves. (2,5) -> min(2,5)*3 = 6, right moves.
# (2,4) -> min(2,4)*2 = 4, right moves. (2,3) -> min(2,3)*1 = 2, right moves.
# Now (3,6) -> min(3,6)*4 = 12, right moves.
# The example test case output '17' for `[2,3,4,5,18,17,6]` is based on `18` and `17` with a width of 1.
# This will be found when `left` is 4 and `right` is 5.
# `left=4, right=5`: `height[4]=18, height[5]=17`. `min_height=17`, `width=1`. `current_area = 17`. `max_area = 17`. `right` moves.
# My expected output of 17 for `[2,3,4,5,18,17,6]` is correct based on the algorithm.

print(f"Input: [0,0,0,0], Output: {sol.maxArea([0,0,0,0])}")
# Expected: 0

print(f"Input: [0,10,0], Output: {sol.maxArea([0,10,0])}")
# Expected: 0