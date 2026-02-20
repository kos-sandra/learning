petya = [int(x) for x in input().split('.')]
vasya = [int(x) for x in input().split('.')]

days_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 0: 31}

if vasya[2] == petya[2]:
    d_months = vasya[1] - petya[1]
else:
    d_months = 12 - petya[1] + vasya[1]

if petya[2] == vasya[2] and petya[1] == vasya[1]:
    total = vasya[0] - petya[0]
else:
    total = days_in_months[petya[1] % 12] - petya[0] + vasya[0]

# print(petya[1], total)

for i in range(1, d_months):
    month = (petya[1] + i) % 12
    total += days_in_months[month]
    # print(month, days_in_months[month])

# print(vasya[1], vasya[0])

print(total)
