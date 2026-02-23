# x, y, z, w = [int(x) for x in input().split()]
# x, y, z = sorted([x, y, z], reverse=True)
# total = 0
#
# for i in range(w // x + 1):
#     ix = i * x
#     for j in range((w - ix) // y + 1):
#         jy = j * y
#         if ix + jy > w:
#             break
#         if (w - ix - jy) % z == 0:
#             total += 1
#
# print(total)

x, y, z, W = [int(x) for x in input().split()]
weights = [x, y, z]
dp = {0: 1}
for weight in weights:
    for w in range(weight, W + 1):
        if w not in dp:
            dp[w] = 0
        dp[w] += dp.get(w - weight, 0)
        print(*[dp.get(i, 0) for i in range(W + 1)])
print(dp[W])

