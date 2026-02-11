# n,m = input().split()
# n,m = int(n), int(m)
# r1 = 0
# r2 = []
# for x in range(n):
#     l = input()
#     for t in l:
#         if t == "B":
#             break
#         if t == ".":
#             r1 += 1
#     r2.append(r1)
#     r1 = 0
# print(min(r2))

n, m = [int(x) for x in input().split()]
print(min([len(input().split('.')) - 1 for i in range(n)]))
