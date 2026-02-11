w, h, r = input().split()
if int(r) <= (int(w) // 2) and int(r) <= (int(h) // 2):
    print('YES')
else:
    print('NO')