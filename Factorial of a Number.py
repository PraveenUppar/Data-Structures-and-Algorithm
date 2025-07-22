def factorial(n):

    # if num is less than zero then return Null
    if n < 0:
        return 0
    
    # if num is equaal to zero then return Null
    elif n == 0:
        return 1
    
    else:
        product = 1
        for i in range(1, n + 1):
            product *= i
        return product

# Test cases
print(f"Factorial of 5: {factorial(5)}")   # Output: 120
print(f"Factorial of 0: {factorial(0)}")   # Output: 1
print(f"Factorial of -3: {factorial(-3)}") 