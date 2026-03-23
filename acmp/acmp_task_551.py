R, r, h, b = [int(x) for x in input().split()]
print("NO" if r*r + ((h+r-b)**2) > R*R else "YES")

