def fibonacci_sequence(n_terms):

    # If the sequenece length is less than or equal to zero return empty list
    if n_terms <= 0:
        return []
    
    # If the n terms is 1 or 2 then the ans will be 0 and 0,1 as sequence starts with [0,1]
    elif n_terms == 1:
        return [0]
    elif n_terms == 2:
        return [0,1]
    
    else:
        # fib sequence starts with [0,1] and this also stores the fib sequence numbers
        list_fib = [0, 1]

        # Loop till the len of sequence is less than the given n terms
        while len(list_fib) < n_terms:
            # next element will the sum of previous two elements
            # In list to get the last element we use list[-1] and for second last element list[-2]
            next_fib = list_fib[-1] + list_fib[-2]
            # Add the next element to the list of fib sequence
            list_fib.append(next_fib)
        return list_fib

# Test cases
print(f"Fibonacci sequence up to 5 terms: {fibonacci_sequence(5)}")   # Output: [0, 1, 1, 2, 3]
print(f"Fibonacci sequence up to 10 terms: {fibonacci_sequence(10)}") # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(f"Fibonacci sequence up to 1 term: {fibonacci_sequence(1)}")    # Output: [0]
