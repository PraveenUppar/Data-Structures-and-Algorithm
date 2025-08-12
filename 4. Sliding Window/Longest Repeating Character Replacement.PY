class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # left pointer 
        left = 0
        # hash map to store the freq of letter
        counter = defaultdict(int)
        # highest freq among the hash map
        max_freq = 0
        # maxmium length found till now
        max_length = 0

        # right pointer iterating the loop
        for right in range(len(s)):
            # if the currenet index element in the hash map is found then ++1
            counter[s[right]] += 1
            # check the highest element present in the hash map till now
            max_freq = max(max_freq,counter[s[right]])
            # Check is the condition is true else move the left pointer
            # (window_size) - max_freq > k 
            if right - left + 1 - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            max_length = max(max_length,right-left+1)
        return max_length
