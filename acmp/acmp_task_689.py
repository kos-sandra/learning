def from_digit_to_symbol(x: int):
    if 0 <= x <= 9:
        return chr(x + ord('0'))
    if 10 <= x <= 36:
        return chr(x - 10 + ord('A'))


def calculate_complexity(x: str):
    return len(x) + len(set(x))


def to_system_sch(x: int, c: int):
    res = ''
    while x > 0:
        symbol = from_digit_to_symbol(x % c)
        res += symbol
        x //= c
    return res[::-1]


def f(x: int, c: int):
    s = to_system_sch(x, c)
    return calculate_complexity(s), c, s


def solution(x: int):
    res = ''
    best_cc = 2
    min_complexity = 200
    for c in range(2, 37):
        s = to_system_sch(x, c)
        complexity_curr = calculate_complexity(s)
        if complexity_curr < min_complexity:
            min_complexity = complexity_curr
            res = s
            best_cc = c
    return best_cc, res


n = int(input())

for i in range(n):
    x = int(input())
    # print(*solution(x))
    print(*min(f(x, i) for i in range(2, 37))[1:])
