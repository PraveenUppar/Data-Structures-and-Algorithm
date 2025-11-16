class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def combinations(index, curr_comb, total):
            # base case: Success
            if total == target:
                result.append(curr_comb[:])
                return 
            # base case: Failure
            if total > target or index == len(candidates):
                return 

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break
                
                curr_comb.append(candidates[i])
                combinations(i + 1, curr_comb, total + candidates[i])
                curr_comb.pop()
        
        combinations(0,[],0)
        return result