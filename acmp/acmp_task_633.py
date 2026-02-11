a = input() + ':'
list = []
for x in range(3):
    list.append(input())
list.sort()
print(a, ', '.join(list))