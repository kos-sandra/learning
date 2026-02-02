n = list(input())
c = []

for x in n:
    c.append(int(x))

c_min = c.copy()
c_max = c.copy()
c_min.sort()


def find_min_in_list_not_zero(a):
    for d in a:
        if d == 0:
            pass
        else:
            return d


if c_min[0] == 0:
    di = find_min_in_list_not_zero(c_min)
    j = c_min.index(di)
    c_min[0], c_min[j] = c_min[j], c_min[0]

c_max.sort(reverse=True)


def convert_to_digit(a):
    res = 0
    for i, x in enumerate(a):
        res += x * 10 ** (len(a) - 1 - i)
    return res


print(convert_to_digit(c_min), convert_to_digit(c_max))
