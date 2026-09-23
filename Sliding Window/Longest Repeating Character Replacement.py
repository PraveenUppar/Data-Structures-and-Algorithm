# You are given a string s consisting of only uppercase english characters and an integer k. 
# You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

def longestrepeat(s, k):
    longest = 0
    left = 0
    hashmap = {}
    max_freq = 0

    for right in range(len(s)):
        hashmap[s[right]] = 1 + hashmap.get(s[right], 0)
        max_freq = max(max_freq, hashmap[s[right]])
        if (right - left + 1) - max_freq > k:
            hashmap[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
    return longest