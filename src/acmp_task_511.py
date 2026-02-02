# n = int(input())-1
# t = [0, 0]
# if n > 144:
#     print("NO")
# else:
#     k = (n // 2) * 10
#     if n % 2 != 0:
#         k += 5
#     t[0] = k // 60
#     t[1] = k - (t[0] * 60)
#     print(t[0], t[1])

i = int(input()) * 5 - 5
if i > 720:
    print('NO')
else:
    print(i // 60, (i % 60))
