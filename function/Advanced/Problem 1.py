# Write a function that calculates the power of a number without using the ** operator.

def power(num, pow):
    result = 1
    for i in range(pow):
        result *= num
    return result

    # if pow < 0:
    #     return 1 / result
    # return result

while True:
    try:
        num = int(input('Enter a number: '))
        pow = int(input('Enter the power: '))
        break
    except ValueError:
        print('Invalid input! Please enter integers only.')

result = power(num, pow)
print(f'The result of {num} raised to the power of {pow} is: {result}')