first = []
second = []
for x in range(4):
    a,b = input().split()
    first.append(int(a))
    second.append(int(b))
if sum(first) == sum(second):
    print('DRAW')
elif sum(first) > sum(second):
    print('1')
else:
    print('2')