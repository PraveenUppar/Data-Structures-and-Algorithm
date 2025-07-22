from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Use a hash map (dictionary in Python) to store counts of numbers
        # This makes lookup for complements very efficient (O(1) on average)
        counts = Counter(nums)
        
        operations = 0
        
        # Iterate through the unique numbers in the counts map
        for num in counts:
            complement = k - num
            
            if complement in counts:
                if num == complement:
                    # If num is its own complement (e.g., k=6, num=3),
                    # we can form pairs using half of its count.
                    # Integer division // 2 ensures we don't count pairs twice.
                    operations += counts[num] // 2
                else:
                    # If num and complement are different,
                    # we can form pairs using the minimum of their counts.
                    # We then "mark" them as used by setting their counts to 0
                    # so they are not recounted when the complement is processed later.
                    operations += min(counts[num], counts[complement])
                
                # Mark both num and its complement as "used" by setting their counts to 0
                # This prevents double-counting pairs (e.g., when processing '2' and then '3' for k=5)
                # and correctly handles cases like k=6, num=3 (already handled by num == complement case)
                counts[num] = 0
                counts[complement] = 0
                
        return operations