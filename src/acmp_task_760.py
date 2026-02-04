n, v, s = [int(x) for x in input().split()]
expected_time = s / v
total_time = expected_time * 60

n_info = [int(x) for x in input().split()]
counter_n = 0

for i in range(1, n*2+1, 2):
    total_time += n_info[i]

print(f'{total_time:.2f}')