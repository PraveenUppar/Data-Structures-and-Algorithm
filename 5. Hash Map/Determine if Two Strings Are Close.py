from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Condition 1: Strings must have the same length.
        # If lengths are different, they cannot be made close.
        if len(word1) != len(word2):
            return False

        # Get character counts for both words
        count1 = Counter(word1)
        count2 = Counter(word2)

        # Condition 2: Both strings must contain the exact same set of characters.
        # If one string has a character not present in the other,
        # we can never transform it (e.g., 'aab' and 'bbc').
        # Compare the keys (characters) of the Counter objects.
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Condition 3: The frequencies of the characters must be the same,
        # when sorted. We can swap characters, meaning we can effectively
        # change a character 'a' to 'b' if 'b' exists, but 'a' must have
        # the same frequency as 'b' had, and 'b' must have the same frequency
        # as 'a' had. This effectively means the *multiset* of frequencies must be identical.
        # Sort the values (frequencies) of the Counter objects and compare them.
        if sorted(count1.values()) != sorted(count2.values()):
            return False

        # If all three conditions are met, the strings are close.
        return True

# Test Cases
sol = Solution()

print(f"word1 = 'abc', word2 = 'bca' -> {sol.closeStrings('abc', 'bca')}")
# Expected: True (Same length, same chars {'a','b','c'}, same frequencies [1,1,1])

print(f"word1 = 'a', word2 = 'aa' -> {sol.closeStrings('a', 'aa')}")
# Expected: False (Different lengths)

print(f"word1 = 'cabbac', word2 = 'abbccc' -> {sol.closeStrings('cabbac', 'abbccc')}")
# count1: {'c': 2, 'a': 2, 'b': 2}, frequencies: [2,2,2]
# count2: {'a': 1, 'b': 2, 'c': 3}, frequencies: [1,2,3]
# set(keys) are {'a','b','c'} for both.
# Sorted frequencies: [2,2,2] vs [1,2,3]. Not equal.
# Expected: False

print(f"word1 = 'aaabbbccc', word2 = 'abcabcabc' -> {sol.closeStrings('aaabbbccc', 'abcabcabc')}")
# count1: {'a': 3, 'b': 3, 'c': 3}, frequencies: [3,3,3]
# count2: {'a': 3, 'b': 3, 'c': 3}, frequencies: [3,3,3]
# Expected: True

print(f"word1 = 'abc', word2 = 'abd' -> {sol.closeStrings('abc', 'abd')}")
# Expected: False (Different set of characters: 'c' vs 'd')

print(f"word1 = 'uau', word2 = 'ssx' -> {sol.closeStrings('uau', 'ssx')}")
# count1: {'u': 2, 'a': 1}, frequencies: [1,2]
# count2: {'s': 2, 'x': 1}, frequencies: [1,2]
# set(keys): {'u','a'} vs {'s','x'}. Not equal.
# Expected: False

print(f"word1 = 'aa', word2 = 'bb' -> {sol.closeStrings('aa', 'bb')}")
# count1: {'a': 2}, frequencies: [2]
# count2: {'b': 2}, frequencies: [2]
# set(keys): {'a'} vs {'b'}. Not equal.
# Expected: False

print(f"word1 = '', word2 = '' -> {sol.closeStrings('', '')}")
# Expected: True (Both empty, all conditions pass)

print(f"word1 = 'zzzaac', word2 = 'abcczz' -> {sol.closeStrings('zzzaac', 'abcczz')}")
# count1: {'z': 3, 'a': 2, 'c': 1}, sorted values: [1, 2, 3]
# count2: {'a': 1, 'b': 1, 'c': 2, 'z': 2}, sorted values: [1, 1, 2, 2] -- Oh wait.
# This test case from LeetCode example should be False
# Corrected manual trace for 'zzzaac' and 'abcczz':
# count1: {'z': 3, 'a': 2, 'c': 1}. Keys: {'z', 'a', 'c'}. Values (sorted): [1, 2, 3]
# count2: {'a': 1, 'b': 1, 'c': 2, 'z': 2}. Keys: {'a', 'b', 'c', 'z'}. Values (sorted): [1, 1, 2, 2]
# Lengths are both 6.
# Set of keys are different (count1 is missing 'b', count2 has 'b').
# This will correctly return False.