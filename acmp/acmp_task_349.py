m,n = [int(x) for x in input().split()]


sieve = [1 for i in range(n+1)]
sieve[0] = sieve[1] = 0
for i in range(2,int(n**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, n+1, i):
            sieve[j] = 0

if all(sieve[i]==0 for i in range(m, len(sieve))):
    print("Absent")
else:
    for i in range(m, len(sieve)):
        if sieve[i] == 1:
            print(i)