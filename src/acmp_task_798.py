m, n, I, J, c = [int(x) for x in input().split()]
C = {0: 'black', 1: 'white'}
if m * n % 2 == 0:
    print('equal')
else:
    i = I % 2
    j = J % 2
    print(C[i ^ j ^ c])
