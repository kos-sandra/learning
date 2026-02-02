n = int(input())
goal = 0
round = 0

while n != 0:
    round = round + 1
    n = n - round
    goal += 1

print(goal)