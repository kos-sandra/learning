# input()
# m = [int(x) for x in input().split()]
# a = -1
# for i in range(len(m)):
#     if m[i] <= 437:
#         a = i + 1
#         break
# if a > 0:
#     print(f'Crash {a}')
# else:
#     print('No crash')

input()
m = [int(x) for x in input().split()]
b = True
for i in range(len(m)):
    if m[i] <= 437:
        b = False
        print(f'Crash {i+1}')
        break
if b:
    print('No crash')