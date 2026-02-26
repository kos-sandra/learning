
N,M,K = [int(x) for x in input().split()]

if 0 not in [N,M,K] and K > 2 and M > 1:
    max_children_in_bus = K - 2
    buses_for_children = (N - 1)// max_children_in_bus + 1
    buses_for_teachers = M // 2
    buses_for_all = (N+M-1) // K + 1

    if buses_for_children <= buses_for_teachers:
        print(buses_for_all)
    else:
        print(0)
    # print(buses_for_children, buses_for_teachers)
else:
    print(0)

