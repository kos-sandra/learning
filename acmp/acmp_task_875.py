def check_neighbour(field, x,y,n,m):
    alive = 0
    for i in range(-1, 2):
        row = (x+n+i) % n
        for j in range(-1,2):
            if i == j == 0:
                continue
            col = (y+m+j) % m
            if field[row][col] == True:
                alive += 1
    return alive


def transform_cell(cell, neighbours):
    if not cell and neighbours == 3:
        return True
    if cell and 1 < neighbours < 4:
        return True
    else:
        return False


def draw_field(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print('*' if field[i][j] else '.', end='')
        print()


n,m,k = [int(x) for x in input().split()]
field = []

for i in range(n):
    row = []
    for x in input():
        row.append(x == '*')
    field.append(row)

for g in range(k):
    tmp = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(transform_cell(field[i][j], check_neighbour(field, i, j, n, m)))
        tmp.append(row)
    field = tmp


draw_field(field)