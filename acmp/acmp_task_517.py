n = int(input())
score = [int(x) for x in input().split()]
total = 0

i = 0

for t in range(10):
    total += score[i]
    strike = score[i] == 10
    spare = score[i] + score[i + 1] == 10 and not strike

    if strike:
        total += score[i + 1] + score[i + 2]
        i += 1
    else:
        total += score[i+1] if not spare else score[i + 1] + score[i + 2]
        i += 2

print(total)