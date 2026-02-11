# n = input()
# if n[0:2] == n[3:1:-1]:
#     print('YES')
# else:
#     print('NO')

n = int(input())
n2 = n // 100
n3 = (n // 10 % 10) + (n % 10)*10
print('YES' if n2 == n3 else 'NO')