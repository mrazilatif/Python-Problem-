# Create a function to check if a given number is prime.

def prime_num(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return 'Not A Prime.'
        else:
            return 'Prime Number.'

while True:
    try:
        num = int(input("Enter the number: "))
        break
    except ValueError:
        print('Number must be an integer.')

print(prime_num(num))