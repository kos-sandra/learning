from math import sin, pi, cos

n, a = [int(x) for x in input().split()]

osn = a / 2
r =  (osn) / sin(pi/n)
r_m = (r ** 2 - osn ** 2) ** 0.5

res = r - r_m
# res = (a / (2 * sin(pi/n))) * (1 - cos(pi/n))

print("YES" if res < 1.0 else "NO")
