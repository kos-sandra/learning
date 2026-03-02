a, b, c = map(set, input().split())

result = a & b & c

print(len(result))
print(*sorted(result))
