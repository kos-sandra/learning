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
    return res

n = int(input())
binary_list = to_binary(n)
print(to_dexi(binary_list))




