
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR*celsius)+32
    return fahrenheit

def main():
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            if temp_type not in ("C","F"):
                raise ValueError("Invalid unit.please enter C or F.")
            if temp_type == 'C':
                fahrenheit = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {fahrenheit:.1f}°F")
            else:
                celsius = convert_to_celsius(temp)
                print(f"{temp}°F is {celsius:.13f}°C")
            break
        except ValueError as e:
            
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
