n = input()

o = 0

for x in n[::-1]:
    if x == str('0'):
        o += 1
    else:
        break

print('1' + '0' * o)

# n = input()
# i = len(n) - 1
# r = 0
# while n[i] == '0':
#     r += 1
#     i -= 1
# print(1, end='')
# for i in range(r):
#     print(0, end='')