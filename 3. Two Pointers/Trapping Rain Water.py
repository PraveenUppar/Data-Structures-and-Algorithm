class Solution:
    def trap(self, height: List[int]) -> int:

        drops = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        while left < right:
            max_left = max(max_left,height[left])
            max_right = max(max_right,height[right])
            if max_left <= max_right:
                left_curr_drop = max_left - height[left]
                drops += left_curr_drop
                left += 1
            if max_right < max_left:
                right_curr_drop = max_right - height[right]
                drops += right_curr_drop
                right -= 1
        return drops


        # # Brute Force - TLE
        # drops = 0

        # for i in range(len(height)):

        #     max_left = height[i]
        #     max_right = height[i]

        #     for j in range(i):
        #         # Find the higest height to the left
        #         max_left = max(max_left,height[j])
        #     for j in range(i+1,len(height)):
        #         # Find the higest height to the right
        #         max_right = max(max_right,height[j])

        #     # height will be determined by the minimum height among the heightest height
        #     # Diff(water that can be stored) to the current index is max_heigth - current_height
        #     curr_drops = min(max_left,max_right) - height[i]
        #     drops += curr_drops

        # return drops
        