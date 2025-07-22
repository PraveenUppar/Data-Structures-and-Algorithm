def sum_of_n_natural_numbers(n):

    if n < 0:
        return 0
    
    total_sum = 0

    # the last number included in the sequence will be (n + 1) otherwise py will default drop the last elemnt that is n
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

# Test cases
print(f"Sum of first 5 natural numbers: {sum_of_n_natural_numbers(5)}")   # Output: 15
print(f"Sum of first 10 natural numbers: {sum_of_n_natural_numbers(10)}") # Output: 55
print(f"Sum of first 0 natural numbers: {sum_of_n_natural_numbers(0)}")   # Output: 0