a, b = input().split()
a, b = int(a), int(b)


# def nod(a, b):
#     a, b = max(a, b), min(a, b)
#     while a % b != 0:
#         a, b = b, a % b
#     return b
#
#
# c = nod(a, b)
# print((a * b) // c)


r1 = max(a, b)
r2 = min(a, b)
l = [r1, r2]
while True:
    l.append(l[-2] % l[-1])
    if l[-1] == 0:
        break
print(l[-2])