n = int(input())
voices = [int(x) for x in input().split()]
voices.sort()
voices = voices[:n // 2 + 1]
# print(voices)
res = 0
for x in voices:
    if x != 1:
        x = x // 2 + 1
    res += x
    # print(x)

print(res)
