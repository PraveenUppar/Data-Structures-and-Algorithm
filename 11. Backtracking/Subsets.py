class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def gensubsets(nums,index,subset,subsets):
            if len(nums) == index:
                subsets.append(subset[:])
                return 
            
            subset.append(nums[index])
            gensubsets(nums, index + 1, subset, subsets)
            subset.pop()

            gensubsets(nums, index + 1, subset, subsets)

        subsets = []
        gensubsets(nums, 0, [], subsets)
        return subsets
        