def get_digits(start, stop, s):
    num = ''
    if start == stop:
        return 1
    for i in range(start, stop):
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
    counts = get_digits(start, letters[i][0], s)
    lc.append((counts, letters[i][1]))
    start = letters[i][0] + 1

line = ''
for i in range(len(lc)):
    line = line + lc[i][1] * lc[i][0]
    while len(line) > 40:
        line_tail = line[40:]
        print(line[:40])
        line = line_tail
if len(line) > 0:
    print(line)
