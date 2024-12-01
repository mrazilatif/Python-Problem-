# Write a function to flatten a nested list.

def flatten(nested_list):
    new_list = []
    for i in nested_list:
        if type(i) == list:
            for val in i:
                new_list.append(val)
        else:
            new_list.append(i)
    return new_list

nested_list = [[1, 2, 3], 'Random', ['apple', 'banana', 'cherry'], [True, False, True], [3.14, 2.71, 1.61]]
print('Flatten list: ', flatten(nested_list))



# ____________________________________________________________________ #

def flatten(nested_list):
    new_list = []
    for i in nested_list:
        if isinstance(i, list):
            new_list.extend(flatten(i))
        else:
            new_list.append(i)
    return new_list

nested_list = [[1, 2, 3], 'Random', ['apple', 'banana', 'cherry'], [True, False, True], [3.14, 2.71, [1.61]]]
print('Flatten list:', flatten(nested_list))
