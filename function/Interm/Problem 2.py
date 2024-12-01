# Write a function to find the nth Fibonacci number using recursion.

def fibonacci(number):
    if number <= 0:
        return "Invalid input. Number must be greater than 0."
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

while True:
    try:
        number = int(input('Enter the number: '))
        break
    except ValueError:
        print('Enter the integer number.')

print(fibonacci(number))