n = int(input())

s = ''
part = ''

for i in range(1, 257):
    part += str(i)
    s += part
    if len(s) >= n:
        break

print(s[n - 1])
