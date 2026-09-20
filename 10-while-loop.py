# a = 1

# while a < 10:
#     print("Hi")
#     a += 1


# b = int(input("Type any Number "))

# while b > 0:
#     print(b % 10)
#     b //= 10


# c = 123
# r = 0

# while c > 0:
#     r = r * 10 + (c % 10)
#     c //= 10
# print(r)


# n = int(input("Pallindromic no checker: "))
# d = n
# r = 0

# while d > 0:
#     r = r * 10 + d % 10
#     d //= 10
# if n == r:
#     print("Yes")
# else:
#     print("No")


import random

num = random.randint(1, 10)
tries = 0

while True:
    guess = int(input("Guess the no between 1 to 10: "))

    if num == guess:
        tries+=1
        print(f"Correct with {tries} tries")
        break
    else:
        tries+=1
        if num<guess:
            print('Wrong, Try little lower')
        else: print('Wrong, Try little higher')
