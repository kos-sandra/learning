k = int(input())
for x in range(k):
    n, m = [int(x) for x in input().split()]
    d = 19 * m + (n + 239) * (n + 366) // 2
    print(d)