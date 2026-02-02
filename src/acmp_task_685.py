s = input().split()
v = [int(s[0]),int(s[1]),int(s[2])]
k = [int(s[3]),int(s[4]),int(s[5])]
v.sort()
k.sort()
o = 0
for i in range(len(v)):
    o += k[i] * v[i]
print(o)