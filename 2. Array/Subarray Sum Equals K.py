class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sub_num = {0:1}
        total = count = 0

        for n in nums:
            total += n
            
            if total - k in sub_num:
                count += sub_num[total-k]
            
            sub_num[total] = 1 + sub_num.get(total, 0)


        # BRUTE FORCE -- TLE
        # count = 0

        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         if curr_sum == k:
        #             count += 1
        # return count
        