n, m, k = map(int, input().split())
# znachki = {"white": 0, "red": 0}
#
# for i in range(1,m+1):
#     w = i // k
#     r = i % k
#     if znachki["white"] < w:
#         znachki["white"] += w - znachki["white"]
#     if znachki["red"] < r:
#         znachki["red"] += r - znachki["red"]
#
# print((znachki["white"]+znachki["red"]) * n)

print(min(m, m // k + k - 1) * n)
