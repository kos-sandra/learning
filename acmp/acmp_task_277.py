def A_(n):
    if n != 0:
        return str(n)
    else:
        return ''


def B_(n: int, chlen: str):
    if n == 0:
        return ''
    s = ''
    n = str(abs(n))
    if n != '1':
        s += n
    return s + chlen


def sign(a,b,c, position):
    if position == 1:
        if b > 0:
            if a == 0:
                return ''
            if a != 0:
                return '+'
        if b < 0:
            return '-'
        if b == 0:
            return ''
    if position == 2:
        if c > 0:
            if a != 0 or b != 0:
                return '+'
            return ''
        if c < 0:
            return '-'
        if c == 0:
            return ''


a,b,c = [int(x) for x in input().split()]


if all(x == 0 for x in [a, b, c]):
    print(0)
else:
    s = A_(a) + sign(a,b,c, 1) + B_(b, 'x') + sign(a,b,c,2) + B_(c, 'y')
    print(s)