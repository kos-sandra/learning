def find(arr, f):
    res = []
    for i in range(len(arr)):
        res.append(f(arr[i]))
    return res


def transpose(arr):
    res = []
    for i in range(len(arr[0])):
        col = []
        for j in range(len(arr)):
            col.append(arr[j][i])
        res.append(col)
    return res


n, m = [int(x) for x in input().split()]

arr = [[int(x) for x in input().split()] for i in range(n)]
arr_t = transpose(arr)

# min_nums = -1000
# max_nums = 1000

# for i in range(n):
#     t = 1000
#     for j in range(m):
#         if arr[i][j] < t:
#             t = arr[i][j]
#     if t > min_nums:
#         min_nums = t
#
# for j in range(m):
#     t = -1000
#     for i in range(n):
#         if arr[i][j] > t:
#             t = arr[i][j]
#     if t < max_nums:
#         max_nums = t
#
# print(min_nums, max_nums)

max_nums = find(arr_t,max)
min_nums = find(arr,min)

print(max(min_nums), min(max_nums))
