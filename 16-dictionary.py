# d = {}
# print(type(d))

# s = {2, "hi", 1}
# print(type(s))

# d2 = {1: "hi", 6: 32, 4: "bye", "hello": "hola", 8:print()}

# print(d2[6])
# print(d2["hello"])

# d2[1] = 100
# print(d2)

# d2.update({50: 500})
# print(d2)

# del d2[4]
# print(d2)

# d2[4] = 100
# print(d2)


# d3 = {1: 11, 3: 33, 5: 55, 6: 66, 9: 99}

# for i in d3:
#     print(i)

# for i in d3:
#     print(i, ":", d3[i])

# for i in d3.values():
#     print(i)

# for i in d3.keys():
#     print(i)

# help(dict)


# d4 = {1: 10, 2: 20, 5: 50, 9: 90}
# d4.clear()
# print(d4)


# # deep copy
# a = [1, 2, 3, 4, 5]
# b = a
# b[0] = 100
# print(a)
# print(b)

# # shallow copy
# a = [1, 2, 3, 4, 5]
# b = a.copy()
# b[0] = 100
# print(a)
# print(b)

# d5 = {1: 10, 6: 60, "hi": "bye"}
# d6 = d5.copy()
# del d6[6]
# print(d5)
# print(d6)


# d7 = {1: 10, 6: 60, "hi": "bye"}
# d8 = d7.get(2)
# print(d8)
# d8 = d7.get(6)
# print(d8)


# d9 = {1: 10, 6: 60, "hi": "bye"}
# print(d9.items())
# print(d9.keys())
# d9.pop(1)
# print(d9)
# d9.popitem()
# print(d9)


# d = {1: 10, 2: 20, 3: 30, 4: 4}
# d2 = {4: 40, 5: 50, 6: 60}

# for i in d2:
#     d[i] = d2[i]
# print(d)


# d = {1: 10, 2: 20, 3: 30, 4: 40}

# sum = 0

# for i in d.values():
#     sum += i
# print(sum)


# l = [1, 1, "hi", 2, 3, 3, 6, 1, 6, 8, 9, "hi", "hi"]

# d = {}

# for i in l:
#     if i in d.keys():
#         d[i] += 1

#     else:
#         d[i] = 1

# print(d)


# d = {1: 10, 2: 20, 3: 30, 4: 440}
# d2 = {4: 40, 5: 50, 6: 60}

# for i in d2:
#     if i in d.keys():
#         d[i] += d2[i]

#     else:
#         d[i] = d2[i]

# print(d)
