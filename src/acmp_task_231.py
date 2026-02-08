def get_digits(start, stop, s):
    num = ''
    if start==stop:
        return 1
    for i in range(start,stop):
        num += s[i]
    return int(num)

s = input()
s = list(s)
letters = []
lc = []

for i in range(len(s)):
    if not s[i].isdigit():
        letters.append((i, s[i]))

start = 0
for i in range(len(letters)):
    counts = get_digits(start,letters[i][0], s)
    lc.append((counts,letters[i][1]))
    start = letters[i][0] +1

for i in range(len(lc)):
    for j in range(1,lc[i][0]+1):
        print(lc[i][1],end='')
        if j%40==0:
            print()
