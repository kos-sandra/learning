import math


c = [int(x) for x in input().split()]
minc = math.ceil(max(c) / 2)
maxc = min(c)
print(minc, maxc)