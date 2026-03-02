
n = int(input()) % 60
fib1 = 1
fib2 = 0

while n+1 > 0:
    fib1, fib2 = fib2, (fib1 + fib2) % 10
    n -= 1
    # print(fib2, end=' ')

print(fib2)