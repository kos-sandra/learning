text = input()
upper = []

if text[0].islower():
    print("No")
else:
    for i in range(len(text)):
        if text[i].isupper():
            upper.append(i)
    upper.append(len(text))

    for i in range(1, len(upper)):
        x = upper[i] - upper[i-1]
        if x > 4 or x < 2:
            print("No")
            break
    else:
        print("Yes")