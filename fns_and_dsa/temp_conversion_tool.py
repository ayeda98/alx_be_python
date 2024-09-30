FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temperature = float(input("Enter the temperature to convert: "))
    operation = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if operation == "F":
        temp_c = convert_to_celsius(temperature)
        print(temperature, "°F is", temp_c, "°C")
    elif operation == "C":
        temp_f = convert_to_fahrenheit(temperature)
        print(temperature, "°C is", temp_f, "°F")
    else:
        print("Invalid operation. Please enter 'C' or 'F'.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
