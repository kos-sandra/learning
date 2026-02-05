def to_dexi(n):
    z = len(n)
    res = 0
    j = 0

    for i in range(z - 1, -1, -1):
        res += n[j] * 2 ** i
        j += 1
    return res

def to_binary(n):
    res = []
    while n >= 2:
        res.append(n%2)
        n //= 2
    res.append(n)
    return res[::-1]


n = int(input())
new = to_binary(n)
max_configuration = 0
configuration = []
for i in range(0,len(new)+1):
    configuration = new[-i:] + new[:-i]
    dexi = to_dexi(configuration)
    if max_configuration < dexi:
        max_configuration = dexi

print(max_configuration)

