n = int(input())
p = [int(x) for x in input().split()]
q = []

index_one = p.index(1)

for i in range(n):
    j = (index_one+i)%(n)
    q.append(p[j])

print(*q)