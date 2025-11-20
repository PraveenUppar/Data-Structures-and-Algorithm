class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(index,nums):

            if index == len(nums):
                result.append(nums[:])
                return 

            seen = set()
            
            for i in range(index,len(nums)):
                
                if nums[i] in seen:
                    continue
                seen.add(nums[i])

                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1, nums)
                nums[index], nums[i] = nums[i], nums[index]

        backtrack(0,nums)
        return result
        