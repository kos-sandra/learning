def len_digit(n):
    n = str(n)
    return(len(n))

def last_digits(n,z):
    n %= (10 ** z)
    return n

a, b = [int(x) for x in input().split()]

for i in range(a,b+1):
    I = last_digits(i ** 2,len_digit(i))
    if i == I:
        print(i, end=' ')
    # print(f'i = {i}, i**2 = {i**2}, last_digits I = {last_digits(i ** 2,len_digit(i))}, len(i) = {len_digit(i)}')