from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Count occurrences of each number
        # Counter creates a dictionary-like object where keys are elements
        # and values are their counts.
        counts = Counter(arr)
        
        # Step 2: Get the list of occurrence counts
        # We only care about the frequencies, not the numbers themselves.
        occurrence_frequencies = list(counts.values())
        
        # Step 3: Check if all these occurrence counts are unique
        # If the length of the list of frequencies is equal to the length of a set
        # created from these frequencies, it means all frequencies are unique.
        return len(occurrence_frequencies) == len(set(occurrence_frequencies))

# Test Cases
sol = Solution()

print(f"Input: [1,2,2,1,1,3], Output: {sol.uniqueOccurrences([1,2,2,1,1,3])}")
# Expected: True (1 appears 3 times, 2 appears 2 times, 3 appears 1 time. All counts (3,2,1) are unique)

print(f"Input: [1,2], Output: {sol.uniqueOccurrences([1,2])}")
# Expected: False (1 appears 1 time, 2 appears 1 time. Counts (1,1) are not unique)

print(f"Input: [-3,0,1,-3,1,1,1,-3,10,0], Output: {sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])}")
# Expected: True (Counts: -3:3, 0:2, 1:4, 10:1. All counts (3,2,4,1) are unique)

print(f"Input: [5,5,5,5], Output: {sol.uniqueOccurrences([5,5,5,5])}")
# Expected: True (5 appears 4 times. Count (4) is unique among itself)

print(f"Input: [1,1,2,2,3,3,3], Output: {sol.uniqueOccurrences([1,1,2,2,3,3,3])}")
# Expected: False (1:2, 2:2, 3:3. Counts (2,2,3) are not unique because 2 repeats)

print(f"Input: [], Output: {sol.uniqueOccurrences([])}")
# Expected: True (No numbers, no counts to be non-unique. Edge case, set will be empty, len will be 0)

print(f"Input: [1], Output: {sol.uniqueOccurrences([1])}")
# Expected: True (1:1. Count (1) is unique) 