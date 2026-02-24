def check_line(x: list, ref):
    return sorted(x) == ref


def i_column(sudoku, i):
    return list(map(lambda x: x[i], sudoku))


n = int(input())
N = n ** 2
ref = list(range(1, N + 1))

sudoku = []
for i in range(N):
    x = [int(x) for x in input().split()]
    sudoku.append(x)

result = True
result &= all(check_line(sudoku[i], ref) for i in range(0, N))
result &= all(check_line(i_column(sudoku, i), ref) for i in range(0, N))
for i in range(n):
    for j in range(n):
        square = []
        for row in sudoku[i * n:i * n + n]:
            square.extend(row[j * n:j * n + n])
        result &= check_line(square, ref)

print('Correct' if result else 'Incorrect')
