class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def backtrack(i, curr_comb):
            if i > n:
                if len(curr_comb) == k:
                    result.append(curr_comb[:])
                return
            
            curr_comb.append(i)
            backtrack(i+1, curr_comb)
            curr_comb.pop()
            backtrack(i+1, curr_comb)

        backtrack(1,[])
        return result