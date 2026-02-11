def gipo(aX,aY,bX,bY):
    cX, cY = aX, bY
    cat1 = max(cX, bX) - min(cX, bX)
    cat2 = max(aY, cY) - min(aY, cY)
    res = (cat1**2 + cat2**2)**0.5
    return res

n, bX, bY, l = [int(x) for x in input().split()]

for i in range(n):
    aX, aY = [int(x) for x in input().split()]
    if gipo(aX,aY,bX,bY) <= l:
        print(i+1)
        break
else:
    print("Yes")
