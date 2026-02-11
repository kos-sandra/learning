# import math
# n = int(input())
# if n <= 0:
#     print('NO')
# elif n == 1:
#     print('YES')
# else:
#     print("YES" if int(math.log2(n)) > int(math.log2(n-1)) else "NO")


n = int(input())
while n > 1 and n % 2 == 0:
    n = n // 2
print('YES' if n == 1 else 'NO')