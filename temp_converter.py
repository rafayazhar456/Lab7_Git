# Temperature Converter
# A small program for practising Git and GitHub.
# It converts a temperature from Celsius to Fahrenheit.
#
# How to run it:  python temperature_converter.py

# Ask the user for a temperature in Celsius
celsius = float(input("Temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32
#Task 5 Kelvin Conversion:
kelvin = celsius+273.5

# Show the result
print("Fahrenheit:", fahrenheit)
print("Kelvin: ", kelvin)
# Change Task 2:
if(fahrenheit<32):
    print("It is below freezing temperature!")