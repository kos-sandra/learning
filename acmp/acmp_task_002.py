# n = int(open('INPUT.TXT').read())
#
# result = 0
# for x in range(1, n + 1) if n > 0 else range(n, 2):
#     result += x
# open('OUTPUT.TXT', 'w').write(str(result))

a, b = [int(x) for x in input().split()]
print(a+b)