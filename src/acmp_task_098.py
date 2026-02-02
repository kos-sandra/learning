n = int(input())
massive = [int(x) for x in input().split()]

player_1 = 0
player_2 = 0

for i in range(n):
    if massive[-1] > massive[0]:
        t = -1
    else:
        t = 0
    r = massive.pop(t)
    if i % 2 == 0:
        player_1 += r
    else:
        player_2 += r

print(player_1, ':', player_2, sep='')
