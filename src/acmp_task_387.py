n = int(input())
r = 0
for x in range(n):
    l = input()
    for i in range(len(l)):
        if l[i] == ">":
            if l[i+1] == l[0]:
                r += 1
print(r)