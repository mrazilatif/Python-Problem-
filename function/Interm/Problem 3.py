# Write a function to check whether a string is a palindrome.

def palindrome(string):
    return 'Its Palindrome' if string == string[::-1] else 'Its Not Palindrome'

string = input('Enter the string to check palindrome or not: ')
print(palindrome(string))