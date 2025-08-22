class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                new_score = stack[-1] * 2
                stack.append(new_score)
            elif i == "+":
                new_sum = stack[-1] + stack[-2]
                stack.append(new_sum)
            else:
                stack.append(int(i))
        return sum(stack)

