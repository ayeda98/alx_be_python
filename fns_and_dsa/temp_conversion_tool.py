FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  
def convert_to_celsius(fahrenheit):
    return float(fahrenheit-32)/FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return float(celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
try :
    temperature = float(input("Enter the temperature to convert: "))
    operation = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
    if operation == "F":
        temp_c = convert_to_celsius(temperature)
        print(temperature, "°F is ",temp_c,"°C")
    elif operation == "C":
        temp_c = convert_to_fahrenheit(temperature)
        print(temperature, "°C is ",temp_c,"°F")

except valueError:
    print("invalid temperature. Please enter a numeric value.")