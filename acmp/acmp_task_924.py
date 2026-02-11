m = []
for x in range(4):
    m.append(input())


def is_bad(m, x, y):
    z = m[x]
    o = m[x + 1]
    v = y + 1
    return z[y] == z[v] and z[y] == o[y] and z[y] == o[v]


found = False

for x in range(0, 3):
    for y in range(0, 3):
        found = found or is_bad(m, x, y)
print('No' if found else 'Yes')

# if mass(m,0,0) or mass(m,0,1) or mass(m,0,2) or mass(m,1,0) or mass(m,1,1) or mass(m,1,2) or mass(m,2,0) or mass(m,2,1) or mass(m,2,2) is True:
