n = int(input())

max_d = 0
cost = 0

while n - 107 >= 0:
    n -= 107
    cost += 7
    max_d += 100

if n > 7:
    max_d += n-7
    cost += 7

print(max_d, cost)