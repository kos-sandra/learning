n = int(input())
k = [int(x) for x in input().split()]

positives = []
negatives = []

for i, x in enumerate(k):
    if x > 0:
        positives.append(i)
    elif x < 0:
        negatives.append(i)

if sum(k[i] for i in positives) > sum(-k[i] for i in negatives):
    print(len(positives))
    for i in positives:
        print(i+1, end=" ")
else:
    print(len(negatives))
    for i in negatives:
        print(i+1, end=" ")