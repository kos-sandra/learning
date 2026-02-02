s = input().split(' ')
n, v, k = int(s[0]), int(s[1]), int(s[2])

# total = 0

# for lit in range(n):
#     today_k = lit * k
#     if today_k >= v:
#         print("NO", total)
#         break
#     total += v - today_k
# else:
#     print("YES", total)

x = (v - 1) // k + 1
last = (v - 1) % k + 1

if n > x:
    print('NO', (v + last) * x // 2)
else:
    print("YES", (v + (v - k * (n - 1))) * n // 2)
