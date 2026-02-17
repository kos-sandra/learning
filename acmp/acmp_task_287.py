n, m = [int(x) for x in input().split()]
line = input()

words = set()

for i in range(n-m+1):
    x = line[i:i+m]
    words.add(x)

print(len(words))