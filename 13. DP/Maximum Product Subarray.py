class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Brute Force
        # res = nums[0]

        # for i in range(len(nums)):
        #     product = nums[i]
        #     res = max(res,product)
        #     for j in range(i + 1, len(nums)):
        #         product = product * nums[j]
        #         res = max(res,product)
        # return res

        # DP

        res = max(nums)
        curr_max = 1
        curr_min = 1

        for num in nums:
            temp = curr_max * num
            curr_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, temp, curr_min * num)
            res = max(res,curr_max)

        return res

