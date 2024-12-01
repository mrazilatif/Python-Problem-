# Create a function that takes a list of numbers and returns the largest number.

# Method 1:

def largest_num(numbers):
    # Assume first num is largest number
    largest_number = numbers[0]
    for i in numbers:
        if i > largest_number:
            largest_number = i
    return largest_number

numbers = [85, 34, 72, 58, 23, 81, 6, 33, 99, 31]
print("The largest number is:", largest_num(numbers))

# ______________________________________________________________________ #

# Method 2:

def largest_num(numbers):
    return max(numbers)

numbers = [85, 34, 72, 58, 23, 81, 6, 33, 99, 31]
print("The largest number is:", largest_num(numbers))
