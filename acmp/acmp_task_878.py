def checking(level):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    for i in range(26):
        if level[i][1] < alphabet[i]:
            return 0
    return 1


n = input()
level = []

for i,x in enumerate(n):
    level.append([i + 1, x])

level.sort(key=lambda x:x[1])

if checking(level):
    print("YES")
    for i, x in enumerate(level):
        if i != 25:
            print(x[0], end=' ')
        else:
            print(x[0])
else:
    print("NO")