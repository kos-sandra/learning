v = [int(x) for x in input().split()]
# p = sum(v)
# t = True
# for x in v:
#     if p - x <= x:
#         t = False
#         break
# print("YES" if t else 'NO')

print('YES' if sum(v) - max(v) > max(v) else 'NO')