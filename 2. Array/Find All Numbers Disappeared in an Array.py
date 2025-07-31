class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # sets are implemented using hash tables (or hash sets). This data structure allows for very fast average-case lookup
        s = set(nums)
        ans = []

        for i in range(1, len(nums)+1):
            if i not in s:
                ans.append(i)
        return ans

        # Brute Force - TLE
        # ans = []
        # n = len(nums)

        # for i in range(1,n+1):
        #     if i not in nums:
        #         ans.append(i)
        # return ans