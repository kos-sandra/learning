n = int(input())
cat_5 = 0
alice_3 = 0

while n > 0:
    if n % 5 == 0:
        n = n - 5
        cat_5 += 1
    else:
        n = n - 3
        alice_3 += 1


print(cat_5, alice_3)