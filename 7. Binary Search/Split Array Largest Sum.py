class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        low = max(nums)
        high = sum(nums)
        ans = high

        def is_possible(nums,mid,k):
            k_count = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    k_count += 1
                    curr_sum = num
                    if k_count > k:
                        return False
            return True

        while low <= high:
            mid = (low + high) // 2
            if is_possible(nums,mid,k):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans