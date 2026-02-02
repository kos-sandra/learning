m = int(input())
if m <= 0 or m > 12:
    print('Error')
elif 3 <= m <= 5:
    print('Spring')
elif 6 <= m <= 8:
    print('Summer')
elif 9 <= m <= 11:
    print('Autumn')
elif m == 12:
    print('Winter')
elif 1 <= m <= 2:
    print('Winter')

###################################

m = int(input())
d = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer',7: 'Summer',8: 'Summer',9: 'Autumn',10: 'Autumn',11: 'Autumn',12: 'Winter'}
if m in d:
    print(d[m])
else:
    print('Error')

##################################

d = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer',7: 'Summer',8: 'Summer',9: 'Autumn',10: 'Autumn',11: 'Autumn',12: 'Winter'}
print(d.get(int(input()), 'Error'))
