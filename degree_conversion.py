# degree_conversion.py
# by Aspen
# Accepts degrees as integer, converts between fahrenheit and celcius, and returns degrees as integer

print("***\nINSTRUCTIONS: This program converts between Celsius and Fahrenheit. First, enter your units, then enter the temperature.\n***\n")

def main():

    def convert():
        input_units = input("Starting units? Please type C or F, then press Enter: ").upper()
        input_temp = float(input("Please type the temperature (ex. 32), then press Enter: "))

        if input_units == "C":
            converted_units = "F"
            converted_temp = input_temp * (9/5) + 32
        elif input_units == "F":
            converted_units = "C"
            converted_temp = (input_temp - 32) * (5/9)
        print("Your converted temperature is:", converted_temp, converted_units)

    convert()

main()
