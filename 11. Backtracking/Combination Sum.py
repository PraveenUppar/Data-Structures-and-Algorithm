class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def combination(candidates,index,subset,subsets):
            total = sum(subset)
            if total == target:
                subsets.append(subset[:])
                return 
            if total > target:
                return 

            for i in range(index, len(candidates)):
                candidate = candidates[i]
                subset.append(candidate)
                combination(candidates, i, subset, subsets)
                subset.pop()

        subsets = []
        combination(candidates,0,[],subsets)
        return subsets

        