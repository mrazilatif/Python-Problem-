# Write a function to find the factorial of a number using recursion.

def factorial(value):
    if value == 0 or value == 1:  # Base case
        return 1
    return value * factorial(value-1)

while True:
    try:
        value = int(input("Enter the number to find its factorial: "))
        break
    except ValueError:
        print("Number must be an integer.")

print(factorial(value))