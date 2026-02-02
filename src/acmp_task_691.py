n = int(input())
d = {'A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y'}
c = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
a = 0
b = 0
for x in range(n):
    s = input()
    if len(s) == 6:
        for i in range(len(s)):
            if i == 0 or i == 4 or i == 5:
                if s[i] in d:
                    a += 1
            if i == 1 or i == 2 or i == 3:
                if s[i] in c:
                    b += 1
        if a + b == 6:
            print('Yes')
        else:
            print('No')
        a = 0
        b = 0
    else:
        print('No')