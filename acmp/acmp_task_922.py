T1, T2, S1, S2, S = [int(x) for x in input().split()]


if S1 >= S:
    print(S)
elif S2 >= S1:
    print("NO")
else:
    v = S1 / T1
    cycle = (S - S2 - 1) // (S1-S2)
    t1 = cycle * (T1 + T2)
    t2 = (S - cycle * (S1 - S2)) / v
    print(t1+t2)