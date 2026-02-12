def without_two_and_more_identical_digits(n):
    s = ''
    for x in n:
        if n.count(x) < 2:
            s += x
        else:
            return ''
    return s


n = int(input())
i = 1
j = 0
element = ''

while j < n:
    element = without_two_and_more_identical_digits(str(i))
    if len(element) > 0:
        j += 1
    i += 1

print(element)
