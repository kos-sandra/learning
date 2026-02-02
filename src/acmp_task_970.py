inp = input().split()
a1, a2, a3 = int(inp[0]), int(inp[1]), int(inp[2])
if a1 + a2 == a3:
    print('YES')
elif a1 + a3 == a2:
    print('YES')
elif a2 + a3 == a1:
    print('YES')
else:
    print('NO')