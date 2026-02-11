n, m = (int(x) for x in input().split())


def solve():
    if n == 0 and m == 0:
        return n, n
    if n < m:
        if n == 0:
            return ['Impossible']
        return m, n + m - 1
    if m == 0:
        return n, n
    return n, n + m - 1

print(*solve())