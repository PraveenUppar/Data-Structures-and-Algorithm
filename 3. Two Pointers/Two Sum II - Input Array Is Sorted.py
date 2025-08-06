class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Two pointer
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left+1,right+1]
            elif curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1

        return []


        #  Brute Force - TLE
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]
        # return []
        