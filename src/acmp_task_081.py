# _ = input()
# a = [int(x) for x in input().split()]
# print(min(a), max(a))

n = int(input())
l = [int(x) for x in input().split()]
min = l[0]
max = 0
for x in l:
    if x < min:
        min = x
    if x > max:
        max = x
print(min, max)