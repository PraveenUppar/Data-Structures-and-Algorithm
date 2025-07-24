class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        element = strs[0]

        for i in range(1,len(strs)):
            j = 0
            while j < min(len(element),len(strs[i])):
                if element[j] != strs[i][j]:
                    break
                j += 1
            element = element[:j]
        return element

        



        