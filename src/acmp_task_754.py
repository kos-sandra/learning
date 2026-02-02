h = [int(x) for x in input().split()]
if 94 <= min(h) and max(h) <= 727:
    print(max(h))
else:
    print('Error')