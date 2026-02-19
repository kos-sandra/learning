n = int(input())
matrix = [input().split() for i in range(n)]
_ = input()
colors_hills = [x for x in input().split()]

total = 0

for i in range(n):
    for j in range(i+1,n):
        if matrix[i][j] == '1' and colors_hills[j] != colors_hills[i]:
            total += 1

print(total)

