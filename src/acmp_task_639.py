n = int(input())
total = []
participants = 0

for i in range(n):
    nn = int(input())
    participants += nn
    for j in range(nn):
        k = input().split()
        k[0] = float(k[0])
        total.append(k)

result = sorted(total, key=lambda x: (-x[0], 0 if x[1].islower() else 1))


print(participants)
for x in result:
    print(f"{x[0]:.2f}", x[1])