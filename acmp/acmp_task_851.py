boys, girls = [int(x) for x in input().split()]
res = ''

while boys > 0 and girls > 1:
    res += 'BGG'
    boys -= 1
    girls -= 2

while boys:
    res += 'B'
    boys -= 1

while girls:
    res += 'G'
    girls -= 1

print(res)

