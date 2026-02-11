def is_lucky(n):
    a = n // 100000 % 10
    b = n // 10000 % 10
    c = n // 1000 % 10
    d = n // 100 % 10
    e = n // 10 % 10
    f = n // 1 % 10
    return a + b + c == d + e + f


k = int(input())
for _ in range(k):
    n = int(input())
    if (is_lucky(n-1) or is_lucky(n+1)) and 0 < n < 999999:
        print('Yes')
    else:
        print('No')

