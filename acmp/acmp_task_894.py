import math

S, R1 = [float(x) for x in input().split()]
R2 = (R1 ** 2 - S / math.pi) ** 0.5
print(round(R2, 3))