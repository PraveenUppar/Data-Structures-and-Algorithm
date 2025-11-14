class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        # Function to generate subset
        def generateSubsets(nums, index, subset, subsets):
            if index == len(nums):
                subsets.append(subset[:])
                return

            # Generate subsets with nums[i]
            subset.append(nums[index])
            generateSubsets(nums, index + 1, subset, subsets)
            subset.pop()

            # Generate subsets without nums[i]
            generateSubsets(nums, index + 1, subset, subsets)

        # Generate all of the subsets
        subsets = []
        generateSubsets(nums, 0, [], subsets)

        # Compute the XOR total for each subset and add to the result
        result = 0
        for subset in subsets:   
            subset_XOR_total = 0
            for element in subset:
                subset_XOR_total ^= element
            result += subset_XOR_total
        return result