def sum_plus_minus(s: list):
    total = 0
    for i in range(len(s)):
        x = int(s[i])
        if i % 2 == 0:
            total += x
        else:
            total -= x
    return total


n = input()
max_diff = sum_plus_minus(n[1:len(n)])
for i in range(1,len(n)):
    s = n[0:i] + n[i+1:len(n)]
    sums = sum_plus_minus(s)
    if sums > max_diff:
        max_diff = sums
    # print(s, sums)

print(max_diff)
