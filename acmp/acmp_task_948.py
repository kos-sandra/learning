k,n = [int(x) for x in input().split()]
p = n // k + 1
o = n % k
if o == 0:
    p -= 1
    o = k
print(p, o)