class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        

        # Brute Force - TLE (O(n∗k))
        # ans = []

        # for left in range((len(nums) - k + 1)):
        #     right = left + k
        #     max_no = max(nums[left:right])
        #     ans.append(max_no)
        # return ans

        