x = float(input())
n = 0
d = 2

while x > 0:
    x = x - 1/d
    d = d + 1
    n += 1

print(n, 'card(s)')