# Create a function that takes two numbers and returns their sum.

def sum_of_numbers(num1, num2):
    return num1 + num2

i = 1
while True:
    try:
        num1 = int(input('Enter the 1st num: '))
        num2 = int(input('Enter the 2nd num: '))
        break
    except ValueError:
        print("Num must be an integer.")


print(sum_of_numbers(num1, num2))