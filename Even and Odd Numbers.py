def check_even_odd(num):
    
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test cases
print(f"Is 4 even or odd? {check_even_odd(4)}")  # Output: Even
print(f"Is 7 even or odd? {check_even_odd(7)}")  # Output: Odd
print(f"Is 0 even or odd? {check_even_odd(0)}")  # Output: Even