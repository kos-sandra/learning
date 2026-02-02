x, y = [int(x) for x in input().split()]

RED = 0
GREEN = 0
BLUE = 0
BLACK = 0


for i in range(1,x+1):
    for j in range(1,y+1):
        if i*j % 5 == 0:
            BLUE += 1
        elif i*j % 3 == 0:
            GREEN += 1
        elif i*j % 2 == 0:
            RED += 1
        else:
            BLACK += 1

print(f"RED : {RED}")
print(f"GREEN : {GREEN}")
print(f"BLUE : {BLUE}")
print(f"BLACK : {BLACK}")

# colors = ["RED", "GREEN", "BLUE", "BLACK"]
# counts = {color: 0 for color in colors}
# divisors = [("BLUE", 5), ("GREEN", 3), ("RED", 2), ("BLACK", 1)]
#
# for i in range(1, x + 1):
#     for j in range(1, y + 1):
#         for color, d in divisors:
#             if i * j % d == 0:
#                 counts[color] += 1
#                 break
#
# for color in colors:
#     print(f"{color} : {counts[color]}")