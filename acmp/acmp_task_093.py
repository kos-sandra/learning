n = int(input())
names = []
result = []
for i in range(n):
    names.append(input())
    result.append(0)

m = int(input())
for i in range(m):
    x = input()
    for j in range(n):
        god = names[j]
        if len(god) != len(x):
            continue
        counter = 0
        for k in range(len(god)):
            if god[k] != x[k]:
                counter += 1
        if counter == 1:
            result[j] += 1

print(*result)
