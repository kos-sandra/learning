# from math import pi
pi = 3.1415
x1, y1 = [int(x) for x in input().split()]
x, y, r = [int(x) for x in input().split()]
polovina_round = (pi*r*r) / 2

h = ((x-x1)**2 + (y-y1)**2)**0.5
s_street = h*r

print(s_street+polovina_round)