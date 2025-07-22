import math # Python's math module has a gcd function

def gcd_of_strings(str1: str, str2: str) -> str:
    # Step 1: Compatibility Check
    # If str1 and str2 can be formed by repeating a common substring 'x',
    # then str1 + str2 must be equal to str2 + str1.
    if str1 + str2 != str2 + str1:
        return ""

    # Step 2: Calculate the GCD of the lengths
    # The length of the common divisor string will be the GCD of their lengths.
    len1 = len(str1)
    len2 = len(str2)
    
    # Use math.gcd for the numerical GCD
    # Eg: len(str1) = 6 and len(str2) = 4 so gcd(4,6) is 2  
    gcd_length = math.gcd(len1, len2)

    # Step 3: Extract the GCD string till the gcd_length from the str1
    # The GCD string is the prefix of either string with the calculated gcd_length.
    return str1[:gcd_length]

# Test Cases
print(f"GCD of ('ABCABC', 'ABC'): '{gcd_of_strings('ABCABC', 'ABC')}'")
print(f"GCD of ('ABABAB', 'ABAB'): '{gcd_of_strings('ABABAB', 'ABAB')}'")
print(f"GCD of ('LEET', 'CODE'): '{gcd_of_strings('LEET', 'CODE')}'")
print(f"GCD of ('ABC', 'ABC'): '{gcd_of_strings('ABC', 'ABC')}'")
print(f"GCD of ('AAAAAA', 'AA'): '{gcd_of_strings('AAAAAA', 'AA')}'")
print(f"GCD of ('TATA', 'TATA'): '{gcd_of_strings('TATA', 'TATA')}'")
