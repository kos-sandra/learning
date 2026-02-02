n = int(input())
if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print(f'12/09/{str(n).zfill(4)}')
else:
    print(f'13/09/{str(n).zfill(4)}')
