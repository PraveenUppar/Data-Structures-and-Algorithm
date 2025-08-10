class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hash_map = {}

        for i in range(len(nums)):
            if nums[i] in hash_map and i - hash_map[nums[i]] <= k:
                return True
            hash_map[nums[i]] = i
        return False

        
        # Brute Force - TLE
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True
        # return False
                    