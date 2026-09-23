# Given a string s and a dictionary of strings wordDict, return true 
# if s can be segmented into a space-separated sequence of dictionary words.

# You are allowed to reuse words in the dictionary an unlimited number of times. 
# You may assume all dictionary words are unique.

def word(s, wordDict):

    wordDict = set(wordDict)
    memo = {}

    def recursion(i):

        if i == len(s):
            return True

        if i in memo:
            return memo[i]

        for j in range(1, len(s)):
            substring = s[i : i + j]
            if substring in wordDict:
                if recursion(j + 1):
                    memo[i] = True
                    return True

        memo[i] = False
        return False


    return recursion(0)