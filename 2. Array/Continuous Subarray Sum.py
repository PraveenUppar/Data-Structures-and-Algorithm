class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        total = 0
        reminder_dict = {0:-1} # Handle edge case if the first element is multiple of k so {0:-1}

        for i,num in enumerate(nums):
            total += num
            reminder = total % k
            # if reminder is not present in reminder_dict
            if reminder not in reminder_dict:
                reminder_dict[reminder] = i  # adds the reminder to its respective index
            # if the reminder is already present in reminder_dict (as hash map does not store duplicate key)
            # calculate the index difference it should be greater than 1 (as given in question)
            elif i - reminder_dict[reminder] > 1:
                return True 
        return False


        # Brute Force - TLE
        # n = len(nums)

        # if n < 2:
        #     return False

        # total = sum(nums)
        # if total % k == 0:
        #     return True

        # for i in range(len(nums)-1):
        #     curr_sum = 0
        #     for j in range(i+1,len(nums)):
        #         curr_sum = sum(nums[i:j+1])
        #         if curr_sum % k == 0:
        #             return True
        # return False
        