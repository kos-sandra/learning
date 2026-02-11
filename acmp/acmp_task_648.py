n = int(input())
cards = [int(x) for x in input().split()]
player = 0
dealer = 0
cards.sort()
for i in range(n):
    if i < n/2:
        dealer += cards[i]
    else:
        player += cards[i]

print(player-dealer)