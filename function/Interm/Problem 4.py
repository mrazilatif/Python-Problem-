# Create a function that takes a list of integers and returns the sum of all even numbers.


# Method 1:

def sum_of_numbers(numbers):
    return sum(numbers)

numbers = [85, 34, 72, 58, 23, 81, 6, 33, 99, 31]
print(sum_of_numbers(numbers))

# ______________________________________________________________________ #

# Method 2:

def sum_of_numbers(numbers):
    number = 0
    for i in numbers:
        number += i
    return number

numbers = [85, 34, 72, 58, 23, 81, 6, 33, 99, 31]
print(sum_of_numbers(numbers))