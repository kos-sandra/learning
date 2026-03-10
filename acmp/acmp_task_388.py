def transpose(array):
    result = [[] for i in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array[i])):
            result[j].append(array[i][j])
    max_values = []
    for i in range(len(result)):
        max_values.append(max(result[i]))
    return max_values


n,m = [int(x) for x in input().split()]

matrix = []
min_values = []

for i in range(n):
     row = [int(x) for x in input().split()]
     min_values.append(min(row))
     matrix.append(row)

max_values = transpose(matrix)
counter = 0

# print(min_values)
# print(max_values)

for i in range(n):
    for j in range(m):
        # print((min_values[i],max_values[j]), end='')
        if min_values[i] == max_values[j]:
            counter+=1
    # print()
# for i in range(n):
#     min_x = min(matrix[i])
#     for j in range(m):
#         max_x = max(trans[j])
#         x = matrix[i][j]
#         if x == min_x and x == max_x:
#             counter += 1
print(counter)

# p = map
# i = lambda: (*p(int, input().split()),)
# n, m = i()
# a = [i() for j in range(n)]
# b = *p(min, a),
# c = p(max, zip(*a))
# print(*(e == d for e in c for d in b))