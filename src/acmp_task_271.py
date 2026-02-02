n = int(input())
d = {}

a,b = 1,1

for i in range(45):
    a,b = b, a+b
    d[b] = i+3

if n in d:
    print("1")
    print(d[n])
else:
    print("0")