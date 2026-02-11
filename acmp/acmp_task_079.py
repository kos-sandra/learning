n,m = [int(x) for x in input().split()]
# r = str(n**m)
# print(r[-1])

# print(n**m%10)

# r = 1
# for x in range(m):
#     r = r * n % 10
#
# print(r)

d = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}
chain = d[n % 10]
print(chain[(m - 1) % len(chain)])