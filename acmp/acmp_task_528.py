n,k = [int(x) for x in input().split()]

total = 0
cur_level = 1

for i in range(k+1):
    total += cur_level
    cur_level += n-2

print(total)