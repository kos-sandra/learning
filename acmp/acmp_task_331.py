h,m = [int(x) for x in input().split(':')]
dh,dm = [int(x) for x in input().split()]
am = m + dm
if am >= 60:
    am -= 60
    dh += 1
ah = (h+dh) % 24
print(f'{str(ah).zfill(2)}:{str(am).zfill(2)}')