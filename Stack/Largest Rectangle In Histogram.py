# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

# Return the area of the largest rectangle that can be formed among the bars.

def rectangle(heights):
    max_area = 0
    stack = []

    for i, height in enumerate(heights):
        start = i
        while stack and stack[-1][1] > height:
            stack_i, stack_h = stack.pop()
            curr_area = stack_h * (i - stack_i)
            max_area = max(max_area, curr_area)
            start = stack_i
        stack.append(start, height)

    for i,h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area