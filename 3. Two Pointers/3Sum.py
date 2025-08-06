class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        # i = index and a = nums[i]
        for i,a in enumerate(nums):

            # if the first pointer is negative then there is no zero sum
            if a > 0:
                break
            
            # if two elements of the first pointer are same then skip 
            if i > 0 and a == nums[i-1]:
                continue
            
            # Two sum approach
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = a + nums[left] + nums[right]
                if curr_sum == 0:
                    ans.append([a, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
        return ans
        

        # Brute Force - TLE

        # ans = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = [nums[i],nums[j],nums[k]]:
        #                 ans.add(tuple(temp))
        # return [list(i) for i in ans]
