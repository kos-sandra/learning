n = int(input())
# mx = n * 6
# mn1 = int(n // 6)
# mn2 = n % 6
# if mn2 == 5:
#     mn2 = 2
# elif mn2 == 4:
#     mn2 = 3
# elif mn2 == 3:
#     mn2 = 4
# elif mn2 == 2:
#     mn2 = 5
# elif mn2 == 1:
#     mn2 = 6
# mn3 = mn1 + mn2
# print(mn3, mx)

print((((((n + 5) // 6) + 1 )* 6) - n), n * 6)
