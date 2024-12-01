# Create a function that accepts a dictionary and returns the key with the highest value.

def get_max_key(data):
    max_key = None
    max_value = float('-inf')
    
    for k, v in data.items():
        if v > max_value:
            max_value = v
            max_key = k
    
    return max_key

example_dict = {1: 50, 2: 75, 3: 60, 4: 90}

max_key = get_max_key(example_dict)
print("Key with the highest value:", max_key)



# _____________________________________________________________ #


def max_key(data):
    if not data:
        return None
    return max(data, key=data.get)

ex_dict = {1: 50, 2: 75, 3: 60, 4: 90}

max_k = max_key(ex_dict)
print("Key with the highest value:", max_k)


