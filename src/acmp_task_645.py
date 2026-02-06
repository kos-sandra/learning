def walls_combi(s):
    nice = n
    res = [0,0]
    for h in range(1,n+1):
        w = s // h
        if h*w or w == 1 > n:
            continue
        p1 = max(h,w) - min(h,w)
        p2 = n - h * w
        if nice > p1 + p2:
            nice = p1 + p2
            res[0] = h
            res[1] = w
    return res


n = int(input())

hw = walls_combi(n)
print(hw[0], hw[1])