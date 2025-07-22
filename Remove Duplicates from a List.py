def remove_duplicates(input_list):
    # Convert to set (removes duplicates) then back to list
    return list(set(input_list)) 

# Test cases
print(f"List with duplicates removed: {remove_duplicates([1, 2, 2, 3, 4, 4, 5])}") # Output: [1, 2, 3, 4, 5] (order not guaranteed)
print(f"List with duplicates removed: {remove_duplicates(['a', 'b', 'a', 'c'])}") # Output: ['a', 'b', 'c']