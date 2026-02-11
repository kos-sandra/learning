n = input()
digit = 1
s = ''

while n not in s:
    s += str(digit)
    digit += 1


print(s.index(n)+1)