n = int(input()) - 1

a = {2, 3, 4, 7, 13}
b = [1, 5, 6, 8, 9]

next_b = b[-1] + 1

while len(a) < n + 1:
    i = len(a)
    new_a = b[i - 1] + b[i - 3]
    a.add(new_a)

    while next_b < new_a +1:
        if next_b not in a:
            b.append(next_b)
        next_b += 1

print(sorted(a)[n])
print(b[n])
