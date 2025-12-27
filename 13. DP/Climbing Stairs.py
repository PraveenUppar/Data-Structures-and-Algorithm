class Solution:
    def climbStairs(self, n: int) -> int:

        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     return dfs(i + 1) + dfs(i + 2)

        # return dfs(0)

        # if n <= 2:
        #     return n

        # a = 1
        # b = 2

        # for i in range(3, n+1):
        #     temp = a + b
        #     a = b
        #     b = temp
        # return b


        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one