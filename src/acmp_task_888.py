n = int(input())
status = input().split()

total = 0
reward = 0

for i in range(n):
    if status[i] == '1':
        reward = max(reward + 1, 3)
        total = total + reward
    else:
        reward = reward - 3

print(total)