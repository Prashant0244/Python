# if else

# a = 15
# b = int(input("No "))
# if b > a:
#     print(f"It is greater than {a}")
# else:
#     print(f"It is smaller than {a}")


# money = int(input('Buy something good with this '))
# if money == 10:
#     print('Chocobar Icecream')
# elif money < 10:
#     print('Toffee')
# else:
#     print('Cake')

# gender = input("Enter M for male and F for female ")
# if gender == "M" or gender == "m":
#     print("Hello Sir")
# elif gender == "F" or gender == "f":
#     print("Hello Madam")
# else:
#     print(f"Hello {gender}")

# number = int(input('Type any positive number '))
# if number >= 0:
#     if number%2 == 0:
#         print('Even Number')
#     elif number%2!=0:
#         print('Odd Number')
# else :
#     print('Invalid Number')

# year = int(input("Type a year "))
# if year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is a Leap Year")
# elif year % 400 ==0:
#     print(f"{year} is a Leap Year")
# else:
#     print("Not a Leap Year")


temp = int(input("Current Temperature "))

if temp < 0:
    print("Freezing Cold")
elif temp >= 0 and temp < 10:
    print("Very Cold")
elif temp >= 10 and temp < 20:
    print("Cold")
elif temp >= 20 and temp < 30:
    print("Pleasant")
elif temp >= 30 and temp < 40:
    print("Hot")
else:
    print("Very Hot")
