# Merging dictionaries using update()
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)


# Merging dictionaries using unpacking operator
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}

# Printing the merged dictionary
print(merged_dict)
