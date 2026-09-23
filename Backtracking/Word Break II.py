# You are given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

def wordbreak(s, wordDict):

    res = []
    wordDict = set(wordDict)

    def backtracking(i, subset):
    
        if i == len(s):
            res.append("".join(subset))
            return

        for j in range(i, len(s)):
            string = s[i: j + 1]
            if string in wordDict:
                subset.append(string)
                backtracking(j + 1, subset)
                subset.pop()

    backtracking(0, [])
    return res