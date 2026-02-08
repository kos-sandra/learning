def to_digit(c):
    return 10 if c == 'A' else int(c)

def to_decimal(x, ss):
    result = 0
    for c in x:
        result = result * ss + to_digit(c)
    return result

ss, k = input().split()
ss = int(ss) % 10 + 2
print(to_decimal(k, ss))