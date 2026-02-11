n = int(input())
time = []
time2 = []

for x in range(n):
    time.append([int(x) for x in input().split()])

time.sort()

for i in time:
    print(*i)
