n = 100
a = 0
b = 1
ss = 8
line_l = 4

for i in range(n):
    print(a % ss, end=('\n' if (i + 1) % line_l == 0 else ' '))
    a, b = b, a + b
