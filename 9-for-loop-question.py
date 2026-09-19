# num = int(input("Write a number "))

# for i in range(1, num+1):
#     print(i)

# for i in range(num, 0, -1):
#     print(i)


# n = 0
# for i in range(num+1):
#     n+=i
# print(n)


# fact=1
# for i in range(num,0,-1):
#     fact*=i
# print(f'Factorial of {num} is: {fact}')


# even = 0
# odd = 0
# for i in range(1, num + 1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print(f"Even Sum = {even} and Odd Sum = {odd}")


# for i in range(1,num+1):
#     if num%i==0:
#         print(i)

# n = 0
# for i in range(1, num):
#     if num % i == 0:
#         n += i
# if num == n:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} not a perfect number")


# if num>1:
#     for i in range(2,num):

#         if num%i==0:
#             print(f'{num} is not a prime no')
#             break
#     else:
#         print(f'{num} is prime no')
# else:
#     print(f'{num} is not a prime no')


# word = input("Write anything to reverse it ")
# print(word[::-1])

# reverse = ""
# for i in range(len(word) - 1, -1, -1):
#     reverse += word[i]
# print(reverse)


# word = input("Check your word is Pallindrome or not:-  ")
# smallWord = word.lower()
# reverse = ""
# for i in range(len(smallWord) - 1, -1, -1):
#     reverse += smallWord[i]
# if reverse == smallWord:
#     print(f'{word} is Pallindrome')
# else: print(f'{word} is not Pallindrome')


word = input('Count Characters, digits and symbols in your word:- ')

char = 0
digit = 0
symbol = 0

for i in range(len(word)):
    if word[i].isalpha():
        char+=1
    elif word[i].isdigit():
        digit+=1
    else:
        symbol+=1

print(f'Characters: {char}\n Digits: {digit}\n Symbols: {symbol}')