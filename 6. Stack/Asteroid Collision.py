from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for i in asteroids:
            # for an asteroid to collide the i < 0 the stack sld not be empty and top element sld be +ve
            while i < 0 and stack and stack[-1] > 0:
                diff = i + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    i = 0
                else:
                    i = 0
                    stack.pop()
            if i:
                stack.append(i)
        return stack