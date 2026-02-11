N, M, F, L = [int(x) for x in input().split()]
n = N - L #всего сдавших
both = M+F-n if M+F > n else 0
math_only = M - both
physics_only = F - both

print(both,math_only, physics_only)

# both - M #не сдавали физику
# both - F #не сдавали матешу
