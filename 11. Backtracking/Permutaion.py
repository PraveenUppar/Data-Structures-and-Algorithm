class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(index,nums):
            if index == len(nums):
                result.append(nums[:])
                return 
            
            for i in range(index,len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index + 1, nums)
                nums[i], nums[index] = nums[index], nums[i]

        backtrack(0,nums)
        return result
        