def formatted_digit_to_cc(n):
    return chr(n + ord('A') - 10) if n > 9 else str(n)


def to_cc(n,cc):
    res = []
    while n > 0:
        res.append(formatted_digit_to_cc(n % cc))
        n = n // cc
    return ''.join(res[::-1])


d,m,y = [int(x) for x in input().split('/')]
cc = d+1
print(to_cc(d,cc),to_cc(m,cc), to_cc(y,cc), sep='/')