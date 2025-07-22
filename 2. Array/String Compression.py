from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        write_idx = 0  # Pointer to where we write the compressed characters
        read_idx = 0   # Pointer to read the original characters

        while read_idx < len(chars):
            current_char = chars[read_idx]
            count = 0

            # Count consecutive occurrences of the current character
            while read_idx < len(chars) and chars[read_idx] == current_char:
                read_idx += 1
                count += 1
            
            # Write the character to the compressed array
            chars[write_idx] = current_char
            write_idx += 1

            # If count is greater than 1, write its digits to the array
            if count > 1:
                for digit in str(count):
                    chars[write_idx] = digit
                    write_idx += 1
        
        return write_idx

# Test Cases
sol = Solution()

# Test Case 1: Basic compression
chars1 = ["a","a","b","b","c","c","c"]
result1 = sol.compress(chars1)
print(f"Input: {['a','a','b','b','c','c','c']}, Output Length: {result1}, Modified Chars (up to length): {chars1[:result1]}")

# Test Case 2: No compression needed
chars2 = ["a"]
result2 = sol.compress(chars2)
print(f"Input: {['a']}, Output Length: {result2}, Modified Chars (up to length): {chars2[:result2]}")

# Test Case 3: Single character repetitions
chars3 = ["a","b","c"]
result3 = sol.compress(chars3)
print(f"Input: {['a','b','c']}, Output Length: {result3}, Modified Chars (up to length): {chars3[:result3]}")

# Test Case 4: Large count
chars4 = ["a","a","a","a","a","a","a","a","a","a","a","a"] # 12 'a's
result4 = sol.compress(chars4)
print(f"Input: {['a'] * 12}, Output Length: {result4}, Modified Chars (up to length): {chars4[:result4]}")

# Test Case 5: Mixed characters and counts
chars5 = ["a","a","a","b","b","c","c","c","c","d"]
result5 = sol.compress(chars5)
print(f"Input: {['a','a','a','b','b','c','c','c','c','d']}, Output Length: {result5}, Modified Chars (up to length): {chars5[:result5]}")

# Test Case 6: Empty input
chars6 = []
result6 = sol.compress(chars6)
print(f"Input: {[]}, Output Length: {result6}, Modified Chars (up to length): {chars6[:result6]}")

# Test Case 7: All same character
chars7 = ["a","a","a","a"]
result7 = sol.compress(chars7)
print(f"Input: {['a','a','a','a']}, Output Length: {result7}, Modified Chars (up to length): {chars7[:result7]}")
