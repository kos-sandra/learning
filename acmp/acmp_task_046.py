o = int(input())



def epsi(n):
    e = '2.7182818284590452353602875'
    E = e.split('.')
    if n < 25:
        a = E[1][n]
    if n == 0:
        print(3)
    elif n == 25:
        print(e)
    elif int(a) >= 5:
        b = str(int(E[1][n-1])+1)
        print(E[0]+'.'+E[1][0:n-1]+b)
    else:
        print(E[0] + '.' + E[1][0:n])

epsi(o)
# for x in range(25):
#     epsi(x)