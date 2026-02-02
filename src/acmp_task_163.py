p = input()

xi = 0
x = 0
for i in range(len(p)):
    if p[i] == 'x':
        xi = i

# try:
#     a = int(p[0])
#     b = int(p[2])
#     c = int(p[4])
# except Exception as e:
#     print(e)

if xi == 0 and p[1] == '+':
    x = int(p[4]) - int(p[2])
elif xi == 2 and p[1] == '+':
    x = int(p[4]) - int(p[0])
elif xi == 0 and p[1] == '-':
    x = int(p[4]) + int(p[2])
elif xi == 4 and p[1] == '+':
    x = int(p[0]) + int(p[2])
elif xi == 2 and p[1] == '-':
    x = int(p[0]) - int(p[4])
elif xi == 4 and p[1] == '-':
    x = int(p[0]) - int(p[2])

print(x)