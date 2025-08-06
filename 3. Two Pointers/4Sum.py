class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curr_sum < target:
                        left += 1
                    elif curr_sum > target:
                        right -= 1
        return ans

        # Brute Force - TLE
        # ans = set()
        # nums.sort()

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1,len(nums)):
        #             for l in range(k + 1,len(nums)):
        #                 if nums[i] + nums[j] + nums[k] + nums[l] == target:
        #                     temp = [nums[i],nums[j],nums[k],nums[l]] # It is in list
        #                     ans.add(tuple(temp)) # Convert to tuple to avoid duplicates
        # return [list(i) for i in ans] # Convert back to list



        # Use set instead of mentioning the condition

        # ans = set()
        # nums.sort()

        # for i in range(len(nums)):
        #     # if i > 0 and nums[i] == nums[i-1]:
        #     #     continue
        #     for j in range(i + 1, len(nums)):
        #         # if j > i + 1 and nums[j] == nums[j-1]:
        #         #     continue

        #         left = j + 1
        #         right = len(nums) - 1

        #         while left < right:
        #             curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
        #             if curr_sum == target:
        #                 temp = [nums[i],nums[j],nums[left],nums[right]]
        #                 ans.add(tuple(temp))
        #                 left += 1
        #                 right -= 1
        #                 while left < right and nums[left] == nums[left - 1]:
        #                     left += 1
        #                 while left < right and nums[right] == nums[right + 1]:
        #                     right -= 1
        #             elif curr_sum < target:
        #                 left += 1
        #             elif curr_sum > target:
        #                 right -= 1
        # return list(ans)

       

