class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        i = (len(nums) // 2)
        return nums[i]

        # Eg: nums = [1,2,1,2,2,3,2,2]

        # nums.sort() = [1,1,2,2,2,2,2,3]
        # n = len(nums) == 8 followed by division 8 // 2 = 4 so from nums[i] which is nums[4] = 2

        # return nums[i] 
        # where i = [len(nums) // 2]