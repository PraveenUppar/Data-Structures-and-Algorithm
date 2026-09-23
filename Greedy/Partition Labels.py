# You are given a string s consisting of lowercase english letters.

# We want to split the string into as many substrings as possible, 
# while ensuring that each letter appears in at most one substring.

# Return a list of integers representing the size of these substrings in the order they appear in the string.

def labs(s):

    last_occurance = {}

    for i, char in enumerate(s):
        last_occurance[char] = i

    res = []
    start = 0
    end = 0

    for i, char in enumerate(s):
        end = max(end, last_occurance[char])

        if i == end:
            res.append(end - start + 1)
            start = i + 1

    return res