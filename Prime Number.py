def is_prime(n):
    
    # Number less than or equal to 1 it is not a prime number 
    if n <= 1:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        # If the number is divisible by range(2,n) then not a prime number
        if n % i == 0:
            return False
        
    # for i in range(2, int(n**0.5) + 1):
    #     if n % i == 0:
    #         return False

    return True

# Test cases
print(f"Is 7 prime? {is_prime(7)}")    # Output: True
print(f"Is 10 prime? {is_prime(10)}")  # Output: False
print(f"Is 1 prime? {is_prime(1)}")    # Output: False
print(f"Is 2 prime? {is_prime(2)}")    # Output: True