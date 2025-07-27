# GCD without usign inbuilt gcd function
def gcd(a,b):
    # Loop will run untill the b is not zero if zero then zero division error
    while b != 0:
        a, b = b, a % b
    # Eg: [a,b] = [a,0]
    return a

print(gcd(7,4))
