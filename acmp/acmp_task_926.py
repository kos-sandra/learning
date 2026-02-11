# n = int(input())
# pole = [input() for i in range(n)]
# cities = []
#
# for i in range(n):
#     for j in range(n):
#         if pole[i][j] == 'C':
#             cities.append([i,j])
#
#
# for x in range(n):
#     if x < n // 2:
#         for y in range(n):
#             if [x,y] in cities[:len(cities) // 2]:
#                 print(1,end='')
#             elif [x, y] in cities[len(cities) // 2 :len(cities)]:
#                 print(2,end='')
#             else:
#                 print(1,end='')
#     if x >= n // 2:
#         for y2 in range(n):
#             if [x, y2] in cities[len(cities) // 2 :len(cities)]:
#                 print(2,end='')
#             elif [x, y2] in cities[:len(cities) // 2]:
#                 print(1, end='')
#             else:
#                 print(2, end='')
#     print()
#
#
# print(pole)
# print(cities)
# print(cities[:len(cities) // 2])
# print(cities[len(cities) // 2 :len(cities)])


n = int(input())
pole = [input() for i in range(n)]
cities = 0
c = 0

for i in range(n):
    for j in range(n):
        if pole[i][j] == 'C':
            cities += 1

for i in range(n):
    for j in range(n):
        if pole[i][j] == 'C':
            c += 1
        if c > cities // 2:
            print(2, end='')
        else:
            print(1, end='')
    print()