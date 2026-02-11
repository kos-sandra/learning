N = int(input())
r = 0
for i in range(N):
    a = input().split()
    for x in a:
        if x == '1':
            r += 1
print(r//2)