k = input().split()
n, w = int(k[0]), k[1]
# l = []
# for i in range(len(w)):
#     if i != n-1:
#         l.append(w[i])
# print(''.join(l))

print(w[:n - 1], w[n:], sep='')
print(f'{w[:n - 1]}{w[n:]}')
print(w[:n - 1] + w[n:])
