m = input()
n = [int(x) for x in m]
if sum(n[:3]) == sum(n[3:]):
    print('YES')
else:
    print('NO')