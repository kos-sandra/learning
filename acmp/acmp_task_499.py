k, w = [int(x) for x in input().split()]
lst = [int(x) for x in input().split()]

# к - количество челоек
# w - ограничение по весу палаток

a1 = lst[0] #вес
b1 = lst[1] #вместимость в чел
a2 = lst[2]
b2 = lst[3]
a3 = lst[4]
b3 = lst[5]

#[(a1, b1), (a2, b2), (a3, b3)]

if a1 + a2 + a3 <= w and b1 + b2 + b3 >= k:
    print('YES')
elif a1 <= w and b1 >= k:
    print('YES')
elif a2 <= w and b2 >= k:
    print('YES')
elif a3 <= w and b3 >= k:
    print('YES')
elif a1 + a2 <= w and b1 + b2 >= k:
    print('YES')
elif a1 + a3 <= w and b1 + b3 >= k:
    print('YES')
elif a2 + a3 <= w and b2 + b3 >= k:
    print('YES')
else:
    print('NO')