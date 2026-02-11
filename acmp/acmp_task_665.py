def str_n(n):
    n = str(n)
    if len(n) == 1:
        n = '0' + n
    return n

def mirror(n):
    n = str_n(n)
    res = n[1]+n[0]
    return res

def is_pallindrome(h,m):
    h = str_n(h)
    if h == m:
        return True
    return False

def find_pallindrome(H,M):
    for h in range(H, H + 12):
        h = (24 + h) % 24
        if M == 59:
            h = (h + 1) % 24
        for m in range(M+1, 60):
            if is_pallindrome(h, mirror(m)):
                res = str_n(h)+':'+str_n(m)
                return res
        M = -1

H, M = [int(x) for x in input().split(':')]

print(find_pallindrome(H,M))