def to_cc(n, c):
    res = []
    while n > 0:
        res.append(n % c)
        n //= c
    return res[::-1]


n = int(input())

for i in range(2, 37):
    res = to_cc(n, i)
    if len(res) == len(set(res)):
        print(i, end=' ')

# res = map(lambda x: (x, to_cc(n,x)),list(range(2,37)))
# res = filter(lambda x: len(x[1]) == len(set(x[1])), res)
# res = map(lambda x: str(x[0]), res)
# print(' '.join(res))
