k = int(input())
left, middle, right = 'GCV'
for i in range(k):
    left, middle, right = right, left, middle
print(left + middle + right)



# k = int(input())
# print('CVGCV'[2 - k % 3: 5 - k % 3])

# k = int(input())
# if k % 3 == 0:
#     print('GCV')
# elif k % 3 == 1:
#     print('VGC')
# elif k % 3 == 2:
#     print('CVG')