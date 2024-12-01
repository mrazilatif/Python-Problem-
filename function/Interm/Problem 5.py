# Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

# Method 1:

import math
def gcd(num1, num2):
    return math.gcd(num1, num2)

print(gcd(12, 18))

# __________________________________________________________________ #

def manual_gcd(a, b):
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    return a

num1 = 12
num2 = 18
print(f"The GCD of {num1} and {num2} is: {manual_gcd(num1, num2)}")