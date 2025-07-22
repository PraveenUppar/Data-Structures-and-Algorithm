def find_largest_element(numbers):

    if not numbers:
        return 0
    return max(numbers)

# Test cases
print(f"Largest in [1, 5, 2, 9, 3]: {find_largest_element([1, 5, 2, 9, 3])}") # Output: 9
print(f"Largest in [-10, -1, -5]: {find_largest_element([-10, -1, -5])}")  # Output: -1
print(f"Largest in []: {find_largest_element([])}")                    # Output: The list is empty.

# max() function to find the maxmium number in the list