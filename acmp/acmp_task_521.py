def manipulation(n):
    if n % 2 == 0:
        return n // 2
    if n % 2 == 1:
        return n * 3 + 1


p, k = [int(x) for x in input().split()]

decks = [p]

while p != k:
    p += 1
    decks.append(p)

touches = 0

for i in range(len(decks)):
    x = decks[i]
    while x > 2:
        x = manipulation(x)
        touches += 1
    decks[i] = x


print(touches)