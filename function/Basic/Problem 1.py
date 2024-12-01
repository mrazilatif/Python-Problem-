# Write a function to calculate the area of a circle given its radius.


import math

def area_of_circle(radius=0):
    pi = math.pi
    return pi * radius ** 2

try:
    radius = int(input('Enter the value of radius to find circle: '))
except ValueError:
    print('Enter the integer!')

print(round(area_of_circle(radius),3))