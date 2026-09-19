# For loop

# a = range(1,21,1)

# for i in a:
#     print(i)

# for i in range(6):
#     print(i)

# for i in range(20, 11, -1):
#     print(i)

# Number Table
# num = int(input('Which table you want? '))

# for i in range(num,(num*10)+1, num):
#     print(i)

# a = "PRASHANT"
# for i in range(len(a)):
#     print(a[i])

# d = 'Wait a min! Who are you?'
# for i in d:
#     print(i)

# for i in range(1, 21):
#     if i == 15:
#         break
#     else:
#         print(i)

# for i in range(1, 21):
#     if i == 15:
#         continue
#     else:
#         print(i)

for i in range(25):

    if i == 21:
        print("break is executed")
        break
    print(i)
else:
    print("break is not executed")
