sus = input().split()
dog = input().split()
holes = int(input())


def dist(a,b):
    ax, ay = int(a[0]), int(a[1])
    bx, by = int(b[0]), int(b[1])
    x = ax - bx
    y = ay - by
    return (x ** 2 + y ** 2) ** 0.5


found = False
for x in range(holes):
    h = input().split()
    gSus = dist(sus,h)
    gDog = dist(dog,h)
    if gSus *2 <= gDog:
        print(x + 1)
        found = True
        break
if not found:
    print('NO')
