n = int(input())


def digits_to_number(l):
    resalt = 0
    for x in l:
        resalt = resalt * 10 + x
    return  resalt


def number_to_digits(n):
    res = []
    if n == 0:
        return [0]
    while n > 0:
        res.append(n % 10)
        n = n // 10
    return res[::-1]


number = n
i = 0

while True:
    digits = number_to_digits(number)
    while len(digits) < 4:
        digits.append(0)
    digits.sort(reverse=True)
    BIG_number = digits_to_number(digits)
    SMALL_number = digits_to_number(digits[::-1])
    new_number = BIG_number - SMALL_number
    if new_number == number:
        break
    number = new_number
    i += 1

print(number)
print(i)