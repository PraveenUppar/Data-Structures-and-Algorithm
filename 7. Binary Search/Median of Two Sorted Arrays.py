class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Formula based = O((m+n)log(m+n))
        merged = sorted(nums1 + nums2)
        length = len(merged)

        if length % 2 == 0:  # even len formula
            return  (merged[length // 2 - 1] + merged[length // 2]) / 2
        else: # odd len formula
            return merged[length // 2]