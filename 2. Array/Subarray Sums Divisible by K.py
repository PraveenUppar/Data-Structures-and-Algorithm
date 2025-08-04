class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        count = 0
        prefix_sum = 0
        prefix_count = {0:1}

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in prefix_count:
                count += prefix_count[remainder]
            prefix_count[remainder] = 1 + prefix_count.get(remainder,0)
        return count


        #  Brute Force - TLE
        # count = 0

        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i,len(nums)):
        #         curr_sum += nums[j]
        #         if curr_sum % k == 0 :
        #             count += 1
        # return count        