# Write a function that takes a list and removes all duplicate elements.

def removeDuplicates(num):
    return list(set(num))

num = [2, 4, 6, 8, 10, 15, 25, 30, 50, 72, 5, 18, 42, 7, 55, 10, 25, 50, 2]
print('List with unique elements:', removeDuplicates(num))


# -------------------------------------------------------------------- #

def removeDuplicates(num):
    new_list = []
    for i in num:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list

num = [2, 4, 6, 8, 10, 15, 25, 30, 50, 72, 5, 18, 42, 7, 55, 10, 25, 50, 2]
print('List with unique elements:', removeDuplicates(num))