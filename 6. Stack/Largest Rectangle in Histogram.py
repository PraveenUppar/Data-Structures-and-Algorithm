class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for index,height in enumerate(heights):
            start = index
            while stack and height < stack[-1][1]:
                stack_i, stack_h = stack.pop()
                curr_area = stack_h * (index - stack_i)
                max_area = max(max_area,curr_area)
                start = stack_i
            stack.append((start,height))
            
        # Remaining in the stack
        for i,h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area

        #  Brute Force = O(n**3)
        # max_area = 0
        # for i in range(len(heights)):
        #     curr_area = 0
        #     height = float("inf")
        #     width = 0 
        #     for j in range(i + 1, len(heights)):
        #         width = j - i + 1
        #         for k in range(i,j+1):
        #             if heights[k] < height:
        #                 height = heights[k]
        #         curr_area = height * width
        #     max_area = max(curr_area,max_area)
        # return max_area