n = input()
a = 'qwertyuiopasdfghjklzxcvbnm'
for i in range(len(a)):
    if a[i] == n:
        print(a[(i+1) % 26])