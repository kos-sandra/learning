def is_simple(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def sort_int(n: int, mode: str):   # asc,desc
    n = sorted(str(n))
    if mode == 'desc':
        n = n[::-1]
    number = 0
    for i in range(len(n)-1,-1,-1):
        number += int(n[i]) * 10**i
    return int(number)


N = input()

if '0' in N:
    print("No")
else:
    min_n = is_simple(sort_int(int(N),"asc"))
    max_n = is_simple(sort_int(int(N),"desc"))
    print("Yes" if min_n == max_n == True else "No")

