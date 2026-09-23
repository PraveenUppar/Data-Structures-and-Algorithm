# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

def sum(nums):
    ans = set()
    nums.sort()

    for i in range(len(nums)):            
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum_total = nums[i] + nums[left] + nums[right]
            if sum_total == 0:
                ans.add(tuple([nums[i], nums[left], nums[right]]))
            if sum_total > 0:
                right -= 1
            else:
                left += 1
    return list(ans)