n = int(input())
score = [int(x) for x in input().split()]
total = 0

tour = 0
while True:

for i,x in enumerate(score):
    if x == 10:
        total += 10 + score[i+1] + score[i+2]
