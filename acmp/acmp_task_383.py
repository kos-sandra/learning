from math import log10

n = int(input())


def razryad(x):
    return int(log10(x)) + 1


def sum_digits(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


def is_nice(x):
    return sum_digits(x) % razryad(x) == 0


count = 0
i = 0
while count < n:
    i += 1
    if is_nice(i):
        count += 1

print(i)