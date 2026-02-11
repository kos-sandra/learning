n = input()
r = 0
for x in n:
    if x == '0':
        r += 1
    if x == '6':
        r += 1
    if x == '8':
        r += 2
    if x == '9':
        r += 1
print(r)