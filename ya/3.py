def is_odd(n):
    if n % 2 != 0:
        return 1
    return 0


N = [4, 6, 22]

for x in N:
    if is_odd(x):
        print('odd')
        break
else:
    print('even')


