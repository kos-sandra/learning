def shift(a):
    res = []
    for i in range(len(a)):
        a = a[1:] + a[0]
        res.append(a)
    return res

a = input()
b = input()

s_b = shift(b)
total = 0

for i in range(len(a) - len(b)+1):
    s_a = a[i: i+len(b)]
    for x in s_b:
        # print(s_a, x)
        if x == s_a:
            total += 1
            break

print(total)

# a = input()
# b = input()
#
# s_b = [b[i:] + b[:i] for i in range(len(b))]
# total = 0
#
# for i in range(len(a) - len(b)+1):
#     total += a[i:i + len(b)] in s_b
#
# print(total)