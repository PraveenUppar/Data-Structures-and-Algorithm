from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float('inf')  
        second = float('inf') 

        # Eg: nums = [1, 2, 3, 4, 5] min1 and min2 = infinity
        #  i = 0; min1 = 1 -- n < infinity so min1 = 1
        #  i = 1; min2 = 2 -- n < infinity so min2 = 2
        #  i = 2; n >min1 and min 2 -- return True

        # Eg: nums = [5, 4, 3, 2, 1] min1 and min2 = infinity
        #  i = 0; min1 = 5 -- n < infinity so min1 = 5
        #  i = 1; min1 = 4 -- n < min1 so min2 = 4
        #  i = 2; min1 = 3 -- n < min1 so min2 = 3
        # The loop will end and return False

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

# Test Cases
sol = Solution()

print(f"Input: [1,2,3,4,5], Output: {sol.increasingTriplet([1,2,3,4,5])}")
print(f"Input: [5,4,3,2,1], Output: {sol.increasingTriplet([5,4,3,2,1])}")
print(f"Input: [2,1,5,0,4,6], Output: {sol.increasingTriplet([2,1,5,0,4,6])}")
print(f"Input: [20,100,10,12,5,13], Output: {sol.increasingTriplet([20,100,10,12,5,13])}")
print(f"Input: [1,5,0,4,1,6], Output: {sol.increasingTriplet([1,5,0,4,1,6])}")
print(f"Input: [1,2], Output: {sol.increasingTriplet([1,2])}")
print(f"Input: [1,1,1,1,1], Output: {sol.increasingTriplet([1,1,1,1,1])}")
print(f"Input: [6,7,1,2], Output: {sol.increasingTriplet([6,7,1,2])}")