# Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.

def convert_temperature(choice, value):
    if choice == 'c':
        Fahrenheit = (value * 9 / 5) + 32
        return Fahrenheit
    elif choice == 'f':
        Celcius = (value - 32) * 5 / 9
        return Celcius
    else:
        return "Invalid choice!"


choice = input("Enter 'C' to select Celsius or 'F' to select Fahrenheit: ").strip().lower()
value = float(input("Enter the temperature value: "))
result = convert_temperature(choice, value)
print(result)
