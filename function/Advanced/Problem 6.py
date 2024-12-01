# Create a function that takes a string and counts the frequency of each character.

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def frequency(string):
    freq = {}
    for i in abc:
        freq[i] = string.lower().count(i)
    return freq

string = 'This method returns the number of times the substring appears in the string.'
print(frequency(string))


# --------------------------------------------------------- #

def count_char_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Example usage:
input_string = "hello"
result = count_char_frequency(input_string)
print(result)
