#Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).

# Function to check if two dictionaries are identical
def are_dicts_identical(dict1, dict2):
    return dict1 == dict2

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict3 = {'a': 1, 'b': 2, 'd': 4}
dict4 = {'a': 1, 'b': 2, 'd': 4}
# Checking if dictionaries are identical
print(are_dicts_identical(dict1, dict2))  # Output: True
print(are_dicts_identical(dict1, dict3))  # Output: False
print(are_dicts_identical(dict3, dict4))  # Output: False