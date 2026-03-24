def solution(x):
    k, n, m, d = x
    a = (d * k * n * m)
    b = (k * n * m - k * n - k * m - n * m)
    if b <= 0 or a % b > 0:
        return -1
    result = a // b
    if result % k == 0 and result % n == 0 and result % m == 0:
        return result
    return -1


print(solution(int(x) for x in input().split()))
