# print("Hello")
# print(10 / 0) # ZeroDivisionError
# print("Hi") # This line of code never run


# num = int(input("Number: "))

# try:
#     print(10 / num)
# except ZeroDivisionError:
#     print("Can't divide by 0")

# print("Done")


# num = int(input("Number: "))

# try:
#     print(10 / num)
# except Exception as err:
#     print(f"Something went wrong; {err}")

# print("Done")


# num = int(input("Number: "))

# try:
#     print(10 / num)
# except Exception as err:
#     print(f"Something went wrong; {err}")
# else:
#     print("Good there is no exception")
# finally:
#     print('Run no matter what')

# print("Done")


# age = int(input("Tell me your age:- "))

# if age < 18 or age > 30:
#     raise ValueError("Age should be between 10 and 30")
# else:
#     print("Welcome to the club")

# print("Race will start soon!")


age = int(input("Tell me your age:- "))

try:

    if age < 18 or age > 30:
        raise ValueError("Age should be between 10 and 30")
    else:
        print("Welcome to the club")

except Exception as err:
    print(f"An error occured as {err}")


print("Race will start soon!")