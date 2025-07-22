def is_palindrome(s):
    return s == s[::-1]

# Test cases
print(f"Is 'madam' a palindrome? {is_palindrome('madam')}")



def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters for robust checking
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]

# Test cases
print(f"Is 'A man, a plan, a canal: Panama' a palindrome? {is_palindrome('A man, a plan, a canal: Panama')}") # Output: True
