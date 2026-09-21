# a = [12, 22, 3.4, True, "python", print()]

# print(a[3])

# print(a[0:4])


# # -> List Traversing

# b = [12, 22, 32, 42, 52, 6.2]

# # 1st way to loop with index
# for i in range(len(b)):
#     print(b[i])

# # 2nd way to loop without accessing index
# for i in b:
#     print(i)


# # -> List Methonds

# print(dir(list))

# help(list)

# l = [9, 1, 3, 4, 5, 4]
# l.append(5)
# l.append("hi")
# l.insert(1, 2)
# l.extend([6, 7, 8])
# l.remove(4)

# print(l)

# popped_item = l.pop(3)
# print(popped_item)

# index = l.index(3)
# print(index)

# count = l.count(4)
# print(count)


# ll = [8, 2, 4, 5, 2, 1]
# ll.sort()
# print(ll)

# ll.reverse()
# print(ll)

# copy = ll.copy()
# print(copy)

# ll.clear()
# print(ll)


# # Question ->

# l = [3, -5, 5, -6, -1, 4, 8, 10]

# positive = []
# negative = []

# for i in range(len(l) - 1, -1, -1):
#     if l[i] > 0:
#         positive.append(l[i])
#     else:
#         negative.append(l[i])

# print(positive, negative)


# for i in l:
#     if i >= 0:
#         positive.append(i)
#     else: negative.append(i)

# print(positive, negative)


# s = [1, 4, 3, 9, 6, 4]

# sum = 0

# for i in range(len(s) - 1, -1, -1):
#     sum += s[i]

# mean = sum / len(s)

# print(mean)


# g = [2, 4, -7, 8, 11, 97, 101, 4, 12, 87]

# greatest = g[0]
# index = 0

# for i in range(len(g) - 1, -1, -1):
#     if g[i] > greatest:
#         greatest = g[i]
#         index = i

# print(index, greatest)


# s = [1, 10, 2, 4, -7, 8, 11, 97, 101, 4, 12, 87, 100]

# greatest = s[0]

# secondG = s[0]

# for i in s:
#     if i > greatest:
#         secondG = greatest
#         greatest = i

#     elif i > secondG:
#         secondG = i

# print(greatest, secondG)


# k = [1, 2, 3, 4, 6, 8, 5]

# g = k[0]

# sort = True

# for i in k:
#     if i >= g:
#         g = i
#     else:
#         sort = False

# print(sort)


# a = [12, 13, 14, 15, 17, 16]

# for i in range(len(a) - 1):
#     if a[i] < a[i + 1]:
#         continue
#     else:
#         print("Not Sorted")
#         break
# else:
#     print("Sorted")
