station = input()
num = int(input())
pos = 0 #текущее состояние
card = num % 2 #остаток по карте
cycle = ['school', 'home', 'school', 'home', 'school'] # 0 1 2 3 4


if station == 'School':
    pos = cycle[0]
    c = 0
else:
    pos = cycle[1]
    c = 1

if station == 'School' and card == 0:
    print("No")
else:
    while pos != "home" or card != 0:
        for x in range(len(cycle[c+1:])):
            pos = cycle[x]
            card -= 1
            if pos == "home" and card == 0:
                break
            elif card == 0:
                card += num % 2
    print("Yes")
