# Create a function to generate a random password of given length, containing uppercase, lowercase, numbers, and special characters.

import random
import string

def gen_pass(length):
    if length < 4:
        return "Password length must be at least 4."
    
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

password = gen_pass(12)
print(f"Password: {password}")