num = input()
num = list(num)

for j in range(2):
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            num.pop(i)
            break
    else:
        num.pop(-1)

print(''.join(num))

