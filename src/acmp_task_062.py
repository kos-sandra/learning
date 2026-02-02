p = input()
l_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
i, j = l_mapping[p[0]], int(p[1])
print('BLACK') if (i + j) % 2 == 0 else print('WHITE')


# p = input()
# l, n = p[0], int(p[1])
# l0 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
# r = {}
# s = l0[l] * n
# for x in range(1, 65):
#     if x % 2 == 0:
#         r[x] = 'WHITE'
#     else:
#         r[x] = 'BLACK'
# if s % 2 == 0:
#     print(r[s])
# else:
#     print(r[s+1])