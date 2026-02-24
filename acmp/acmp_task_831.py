def is_simple(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def digits_from_number(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


a, b = [int(x) for x in input().split()]

simple_numbers = []
max_sum = 0

for i in range(a, b + 1):
    if is_simple(i):
        commy = digits_from_number(i)
        simple_numbers.append([commy, i])
        if max_sum < commy:
            max_sum = commy

simple_numbers = list(filter(lambda x: x[0] == max_sum, simple_numbers))
if len(simple_numbers) == 0:
    print(-1)
else:
    print(max(simple_numbers, key=lambda x: x[1])[1])
