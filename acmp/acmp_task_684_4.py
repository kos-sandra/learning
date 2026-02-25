a, b, c, d, e = map(ord, input())
z = abs(d - a) - e + b
print(['YES', 'NO'][z % 2 or z > 0])
