# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. 
# Return the median value among all elements of the two arrays.

def findmedian(nums1, nums2):

    merge_arr = sorted(nums1, nums2)
    mid = len(merge_arr) // 2

    if len(merge_arr) % 2 == 0:
        ele1 = merge_arr[mid]
        ele2 = merge_arr[mid - 1]
        median = (ele1 + ele2) / 2
        return median
    else:
        return merge_arr[mid]