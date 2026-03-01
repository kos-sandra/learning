n = input()

if len(n) < 3:
    print(0)
else:
    res = []

    for i in range(len(n)):
        if n[i] != '0':
            for j in range(i+1,len(n)):
                for k in range(j+1,len(n)):
                    s = n[i] + n[j] + n[k]
                    res.append(s)
    print(len(set(res)))