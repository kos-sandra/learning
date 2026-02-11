N = input()
r = ''
f = [0, 1]
for i in range(24):
    f.append(f[i] + f[i+1])
for z in f[2:]:
    if z <= len(N):
        r += N[z-1]
print(r)