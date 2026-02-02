salary = input().split()
a,b,c = [int(x) for x in salary]
if a < b and a < c:
    min = a
    max = b if c < b else c
elif b < c:
    min = b
    max = c if a < c else a
else:
    min = c
    max = b if a < b else a
print(max - min)

# salaries = [int(x) for x in input().split()]
# print(max(salaries) - min(salaries))