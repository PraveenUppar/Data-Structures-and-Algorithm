class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(i,curr):
            if i == len(s):
                result.append(curr[:])
                return 
            for j in range(i,len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    curr.append(substring)
                    backtrack(j+1,curr)
                    curr.pop()
        backtrack(0,[])
        return result
        