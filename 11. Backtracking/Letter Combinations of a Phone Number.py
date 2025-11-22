class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        result = []
        Char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index,curr):
            if len(curr) == len(digits):
                result.append(curr)
                return
            for c in Char[digits[index]]:
                backtrack(index + 1, curr + c)
                
        backtrack(0,"")
        return result 
        