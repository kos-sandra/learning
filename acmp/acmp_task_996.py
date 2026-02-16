# n = int(input())
# p = [1]
# k = 2
#
#
# def is_in(array, x):
#     l = 0
#     r = len(array) - 1
#     if x == array[r]:
#         return True
#     while True:
#         m = (r + l) // 2
#         y = array[m]
#         if x == y:
#             return True
#         if x > y:
#             l = m
#         else:
#             r = m
#         if r - l < 2:
#             return False
#
#
# while len(p) != n:
#     if is_in(p, k):
#         p.append(p[k - 2] + 3)
#     else:
#         p.append(p[k - 2] + 2)
#     k += 1
#
# print(p[-1])

n = int(input())
p = 1
s = {1}

for i in range(2,n+1):
    p = p + (3 if i in s else 2)
    s.add(p)

print(p)

