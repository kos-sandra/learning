n = int(input())
vhod = [int(x) for x in input().split()]
perestanovka = 0

for i in range(n):
    if i != n-1:
        if vhod[i] - vhod[i+1] != -1:
            perestanovka += 1
    else:
        break

print(perestanovka)