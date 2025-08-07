class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # handle edge case wheere k > len(nums)
        k = k % len(nums)
        if k == 0:
            return nums
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        # [1,2,3,4],[5,6,7] = [5,6,7],[1,2,3,4]
        return nums
        
        # Eg: [1,2,3,4,5,6,7] k = 3
        # nums[-3:] becomes [5, 6, 7].
        # nums[:-3] becomes [1, 2, 3, 4].
        # nums[:3], nums[3:] = [5, 6, 7], [1, 2, 3, 4] 