from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Elements in nums1 that are not in nums2
        diff1 = list(set1 - set2)
        
        # Elements in nums2 that are not in nums1
        diff2 = list(set2 - set1)
        
        return [diff1, diff2]

# Test Cases
sol = Solution()

print(f"nums1 = [1,2,3], nums2 = [2,4,6] -> {sol.findDifference([1,2,3], [2,4,6])}")
# Expected: [[1,3],[4,6]] (Order of elements within sub-lists might vary due to set conversion)

print(f"nums1 = [1,2,3,3], nums2 = [1,1,2,2] -> {sol.findDifference([1,2,3,3], [1,1,2,2])}")
# Expected: [[3],[]]

print(f"nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10] -> {sol.findDifference([1,2,3,4,5], [6,7,8,9,10])}")
# Expected: [[1,2,3,4,5],[6,7,8,9,10]]

print(f"nums1 = [], nums2 = [1,2,3] -> {sol.findDifference([], [1,2,3])}")
# Expected: [[],[1,2,3]]

print(f"nums1 = [1,2,3], nums2 = [] -> {sol.findDifference([1,2,3], [])}")
# Expected: [[1,2,3],[]]

print(f"nums1 = [], nums2 = [] -> {sol.findDifference([], [])}")
# Expected: [[],[]]

print(f"nums1 = [1,1,1], nums2 = [1,1,1] -> {sol.findDifference([1,1,1], [1,1,1])}")
# Expected: [[],[]]