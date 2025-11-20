class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        nums.sort()

        def backtrack(index,subset):
            if len(nums) == index:
                subsets.append(subset[:])
                return

            subset.append(nums[index])
            backtrack(index + 1,subset)
            subset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
                
            backtrack(index + 1,subset)
            
        backtrack(0,[])
        return subsets 