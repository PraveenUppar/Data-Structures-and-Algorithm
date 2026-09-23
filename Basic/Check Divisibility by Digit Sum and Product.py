# You are given a positive integer n. 
# Determine whether n is divisible by the sum of the following two values:

# The digit sum of n (the sum of its digits).
# The digit product of n (the product of its digits).
# Return true if n is divisible by this sum; otherwise, return false.

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n 
        digit_sum = 0
        digit_product = 1

        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_product *= digit
            n //= 10

        divisor = digit_sum + digit_product
        return original % divisor == 0