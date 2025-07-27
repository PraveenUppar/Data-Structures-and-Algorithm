class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        ### Inbuilt Function

        nums.sort()
        return nums

        ###

        ### Selection Sort - TLE

        # n = len(nums)

        # for i in range(n - 1):
        #     min_idx = i
        #     for j in range(i + 1, n):
        #         if nums[j] < nums[min_idx]:
        #             min_idx = j
        #     nums[i], nums[min_idx] = nums[min_idx], nums[i]
        # return nums

        