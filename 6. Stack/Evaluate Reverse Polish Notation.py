class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # arithmetic expression = 3 + 6 = 9
        # operator is + and operands are 3 and 6

        stack = []

        for i in tokens:
            if i == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                res = val1 + val2
                stack.append(res)
            elif i == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                res = val2 - val1
                stack.append(res)
            elif i == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                res = val1 * val2
                stack.append(res)
            elif i == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                res = int(float(val2) / val1)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]