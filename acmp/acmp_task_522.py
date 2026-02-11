M, N = [int(x) for x in input().split()]
m = [int(x) for x in input().split()]
n = [int(x) for x in input().split()]

mm = set(m)
nn = set(n)

if mm == nn:
    print(1)
else:
    print(0)