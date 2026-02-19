W, H = [int(x) for x in input().split()]

m1 = [input() for _ in range(H)]
m2 = [input() for _ in range(H)]

key = [x for x in input()]

trullyyyy = {
    '00': key[0],
    '01': key[1],
    '10': key[2],
    '11': key[3]
}


for i in range(H):
    for j in range(W):
        s = m1[i][j] + m2[i][j]
        print(trullyyyy[s], end='')
    print()