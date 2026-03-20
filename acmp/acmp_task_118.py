def run(start_i, array, kill):
    K = 0
    while K < kill:
        start_i = (start_i + 1) % len(array)
        if array[start_i]:
            K += 1
    return start_i


n, k = [int(x) for x in input().split()]

men = [1 for i in range(n)]
kill = -1
alive = n

while alive > 0:
    kill = run(kill,men,k)
    men[kill] = 0
    alive -= 1

print(kill + 1)


# n, k = map(int, input().split())
# j = lambda n, k: 1 if n == 1 else (j(n-1, k) + k - 1) % n + 1
# print(j(n, k))
