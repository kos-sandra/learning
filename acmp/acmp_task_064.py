def is_simple(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


def add_simple_digits(index):
    res = ''
    digit = 2
    while len(res) < index:
        if is_simple(digit):
            res += str(digit)
        digit += 1
    return res


n = int(input())
find_indexes = [int(x) for x in input().split()]

max_digit = max(find_indexes)
simple_sequence = add_simple_digits(max_digit)

for index in find_indexes:
    print(simple_sequence[index - 1], end='')
