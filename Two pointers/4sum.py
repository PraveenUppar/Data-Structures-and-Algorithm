# You are given an integer array nums of size n, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

def sum(nums, target):
    ans = set()
    nums.sort()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            left = j + 1
            right = len(nums) - 1

            while left < right:
                sum_total = nums[i] + nums[j] + nums[left] + nums[right]
                if sum_total == target:
                    ans.add(tuple([nums[i], nums[j], nums[left], nums[right]]))
                    right -= 1
                    left += 1
                elif sum_total > target:
                    right -= 1
                else:
                    left += 1
    return list(ans)