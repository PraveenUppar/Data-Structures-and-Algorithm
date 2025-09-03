class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x 
        res = 0

        while left <= right:
            i = left + (right - left) // 2
            if i * i > x:
                right = i - 1
            elif i * i < x:
                left = i + 1
                res = i
            else:
                return i
        return res          

        # Brute Force O(n)
        # if x == 0:
        #     return 0
        # res = 0
        # for i in range(1, x + 1):
        #     if i * i > x:
        #         return res
        #     res = i
        # return res

        # Built-in function
        # return int(x ** 0.5)