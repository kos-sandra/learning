def set_numbers(array):
    set = []
    len_a = len(array)
    for x in array:
        if x not in set:
            set.append(x)
    return set


n = int(input())
for i in range(n):
    a,b = input().split()
    set_a = set_numbers(a).sort()
    set_b = set_numbers(b).sort()
    if set_a == set_b:
        print("YES")
    else:
        print("NO")