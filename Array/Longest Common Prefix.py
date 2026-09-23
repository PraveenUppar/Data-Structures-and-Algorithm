# You are given an array of strings strs. Return the longest common prefix of all the strings.

# If there is no longest common prefix, return an empty string "".

def longest(strs):

    if not strs:
        return ""

    ans = ""

    for i in range(len(strs[0])):
        char_check = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char_check:
                return ans 
        ans += char_check
    return ans