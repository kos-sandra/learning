n = int(input())


def inc(digits):
    digits[0] += 1
    i = 0
    while digits[i] == 10:
        if i == len(digits) - 1:
            digits.append(0)
        digits[i] = 0
        digits[i + 1] += 1
        i += 1


def is_nice(digits):
    return sum(digits) % len(digits) == 0


digits = [0]
count = 0

while count < n:
    inc(digits)
    if is_nice(digits):
        count += 1

print(''.join([str(d) for d in digits[::-1]]))