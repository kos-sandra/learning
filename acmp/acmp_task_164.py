n = input()

def numerology(number): #str(number)
    total = 0
    for d in number:
        total += int(d)

    if total > 9:
        total = numerology(str(total))

    return total


ln = len(n)

if ln <2:
    print("NO")
else:
    for i in range(ln):
        if numerology(n[:i]) == numerology(n[i:]):
            print("YES")
            break
    else:
        print("NO")



