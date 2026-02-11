s, p = (int(x) for x in input().split())
# found = False
# for i in range(1,1001):
#     if found:
#         break
#     for j in range(i,1001):
#         if i + j == s and i * j == p:
#             print(i,j)
#             found = True
#             break

d = s**2 - 4*p
x = (s - d ** 0.5) / 2
y = (s + d ** 0.5) / 2
print(int(x),int(y))