from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = []

        for i in nums:
            if i == val:
                continue
            arr.append(i)

        for j in range(len(arr)):
            nums[j] = arr[j]:
        return len(nums)
        