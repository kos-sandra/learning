N, i, j = [int(x) for x in input().split()]
r = 0
if j > i:
    if j - i <= N // 2:
        r = j - i - 1
    else:
        r = N - j + i - 1
else:
    if i - j <= N // 2:
        r = i - j - 1
    else:
        r = N - i + j - 1
print(r)