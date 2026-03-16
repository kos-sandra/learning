def ost_bottle(n, array):
    for x in array[:n]:
        array.remove(x)
    return array


n, k = [int(x) for x in input().split()]

c = [int(x) for x in input().split()]
c.sort(reverse=True)

total = 0
for i in range((n-1)//k+1):
    total += sum((i + 1) * x for x in c[:k])
    # print(c[:k], i, sum((i + 1) * x for x in c[:k]), end = ' ')
    c = ost_bottle(k, c)
    # print(c, total)
print(total)
