from covernter import celsius_to_fahrenheit
print("Temperature Converter")


try:
    celsius = float(input("Enter a temperture in Celsius: "))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"{celsius}C is equal to {fahrenheit}F")

except ValueError:
    print("invalid input. Please enter a number.")