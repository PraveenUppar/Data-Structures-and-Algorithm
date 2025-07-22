def is_leap_year(year):

    # check 2 condition
    # Either it shoule be divible by 4 but not by 100
    # Or it should be divisble by 400

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test cases
print(f"Is 2000 a leap year? {is_leap_year(2000)}") # Output: True (divisible by 400)
print(f"Is 2004 a leap year? {is_leap_year(2004)}") # Output: True (divisible by 4)
print(f"Is 1900 a leap year? {is_leap_year(1900)}") # Output: False (divisible by 100 but not 400)
print(f"Is 2023 a leap year? {is_leap_year(2023)}") # Output: False