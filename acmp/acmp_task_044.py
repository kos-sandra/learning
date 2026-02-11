k = input()
r = 0
for i in range(len(k)-3):
    if k[i:i+5] == ">>-->" or k[i:i+5] == "<--<<":
        r += 1
print(r)