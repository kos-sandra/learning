def do_digits(x):
    if '0' in str(x):
        return [0]
    res = []
    while x > 0:
        res.append(x % 10)
        x //= 10
    return res


def mult(array):
    if 0 in array:
        return 0
    res = 1
    for x in array:
        res *= x
    return res


def solution(x):
    m = mult(do_digits(x))
    if m == 0:
        return False
    return x % m == 0

l,r = [int(x) for x in input().split()]

print(sum([solution(i) for i in range(l, r+1)]))