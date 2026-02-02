n = int(input())
a = [int(x) for x in input().split()]
k = int(input())
print(sum([min(x, k) for x in a]))