# Write a function to count the vowels in a given string.

def vowels(string):
    count = 0
    for i in string:
        if i in ['a','e','i','o','u']:
            count += 1
    return count

string = input('Enter the string to check vowels: ')
print(vowels(string))