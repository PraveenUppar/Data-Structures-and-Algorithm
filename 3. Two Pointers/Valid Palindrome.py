class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_string = ""

        for char in s:
            if char.isalnum():
                new_char = char.lower()
                clean_string += new_char
        return clean_string == clean_string[::-1]
        
# isalnum() method in Python is a built-in string method used to check if all characters in a string are alphanumeric   

# The given input string is not clean contians spaces ans non alphanumeric values
# Convert the given input string into cleaned string by s.lower and s.isalnum()
# reverse the cleaned string 
# Compare the revered_clean_string with the clean_string