#Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.

original_dict = {'z': 1, 'a': 2, 'c': 3}

# Sorting the dictionary by keys in ascending order
sorted_dict = {key: original_dict[key] for key in sorted(original_dict)}

# Printing the sorted dictionary
print(sorted_dict)
