class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m]
        i = 0

        while i < n:
            nums1.append(nums2[i])
            i += 1
        nums1.sort()
        return(nums1)
        