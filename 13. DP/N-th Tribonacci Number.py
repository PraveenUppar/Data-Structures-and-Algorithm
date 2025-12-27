class Solution:
    def tribonacci(self, n: int) -> int:

        # algo
        # declare t0 = 0 | t1 = 1 | t2 = 1
        # check for n if less than 3 then return the res
        # func - take the n-1 | n-2 | n-3 as para and return 
        # res = [] -- store the n-i value
        # we know that t1 = 1 and t2 = 1
        # append the values in the res arr
        # loop from the range 3 to n + 1 (i = 0, 1, 2) == res[0,1,1]
        # 

        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 1
        # else:
        #     return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        res = [0] * (n + 1)
        res[0] = 0
        res[1] = 1
        res[2] = 1

        for i in range(3,n+1):
            res[i] = res[i-1] + res[i-2] + res[i-3]
        return res[n]

