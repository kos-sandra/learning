n, m = [int(x) for x in input().split()]
log_burning_time = [int(x) for x in input().split()]

available_burning_time = sum(log_burning_time) - n + 1

if available_burning_time < m or max(log_burning_time) > m:
    print("no")
else:
    print("yes")




