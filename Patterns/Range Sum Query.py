class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * (len(nums))
        prev_sum = 0

        for i in range(len(nums)):
            self.prefixSum[i] = prev_sum + nums[i]
            prev_sum += nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left-1]
       

