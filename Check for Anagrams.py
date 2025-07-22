def are_anagrams(str1, str2):
    # Clean strings: convert to lowercase and remove spaces
    cleaned_str1 = (sorted(str1))
    cleaned_str2 = (sorted(str2))
    
    return cleaned_str1 == cleaned_str2

# Test cases
print(f"Are 'listen' and 'silent' anagrams? {are_anagrams('listen', 'silent')}") # Output: True
print(f"Are 'hello' and 'world' anagrams? {are_anagrams('hello', 'world')}")   # Output: False

# Two words are anagrams if they contain the same characters with the same frequencies, but in a different order (e.g., "listen" and "silent").``