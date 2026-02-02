s = input()
# p = 1
# for x in s:
#     if x == 'A':
#         if p == 1:
#             p = 2
#         elif p == 2:
#             p = 1
#     if x == 'B':
#         if p == 2:
#             p = 3
#         elif p == 3:
#             p = 2
#     if x == 'C':
#         if p == 1:
#             p = 3
#         elif p == 3:
#             p = 1
# print(p)

p = 1
d = {
    1: {'A': 2, 'B': 1, 'C': 3},
    2: {'A': 1, 'B': 3, 'C': 2},
    3: {'A': 3, 'B': 2, 'C': 1}
}
for x in s:
    p = d[p][x]
print(p)