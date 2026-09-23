# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

def longestsubstring(s):
    longest = 0
    left = 0
    curr = set()

    for right in range(len(s)):
        while s[right] in curr:
            curr.remove(s[left])
            left += 1
        curr.add(s[right])
        longest = max(longest, len(curr))
    return longest