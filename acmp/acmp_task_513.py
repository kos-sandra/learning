# def factorial(x):
#     total = 1
#     for i in range(1,x+1):
#         total *= i
#     return total
#
#
# def c(n,k):
#     return factorial(n) // (factorial(n-k) * factorial(k))


n = int(input())

print(2**n - n - 1)