# n = int(input())
# a = [int(x) for x in input().split()]
# b = []
# for i in range(len(a)):
#     b.append(a[n-1-i])
# for f in b:
#     print(f, end=' ')

# input()
# l = input().split()
# print(*l[:: -1])

t, a = input(), input().split()
[print(a[len(a) - i - 1], end=' ') for i in range(len(a))]