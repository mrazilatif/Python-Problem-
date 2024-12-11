#Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.

std = {
    "name" : "Malik",
    "grade" : "A+",
    "age" : "19",
    "city" : "New-Year"
}

print(std)
#Access the value of the key grade in the student dictionary.
#grade_value = std["grade"]
#print(grade_value , std )

#city_name = std["city"]
#print(city_name , std)

#Update the value of the age key in the student dictionary to 20.
#std["age"] = 20
#print(std)

#Remove the key city from the student dictionary.
#del std["city"]
#print(std)

#Iterate through the dictionary student and print all keys.

for keys in std:
    print(keys)