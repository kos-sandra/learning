n = int(input())
nums = [int(x) for x in input().split()]

nums_counts = [0]*201

for x in nums:
    nums_counts[x] += 1

res = []

for i in range(-100, 101):
    res.extend([i]*nums_counts[i])

print(*res)
