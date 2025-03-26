
print("Namaste python user\n")

# type casting
number = int("10")
floating_num = float(number)
string_value = str(10)

# condition
age = int(input("Enter your age"))
if type(age) != int:
    print("Invalid")
if age > 18 and True :
    print("You are eligible")
else:
    print("You are not eligible")

day_name = input("Enter day name")
if day_name == "sun":
    print("Sunday")
elif day_name == "mon":
    print("Monday")
elif day_name == "tue":
    print("tuesday")
else:
    print("another day")

# switch cases

# Python version 3.9 does not support match statements
# command = input("Enter city code")
# match command:
#     case "ADI":
#         print("Ahmedabad")
#     case "KNW":
#         print("Khandwa")
#     case _:
#         print("Another city")

