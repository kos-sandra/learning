n = int(input())
friends_from = []

for i in range(n):
    friends_from.append(input())

m = int(input())
friends_to = []

for i in range(m):
    friends_to.append(input())

friends_from.sort()
friends_to.sort()
print(f'Friends: {", ".join(friends_from)}')
print(f'Mutual Friends: {", ".join(f for f in friends_to if f in friends_from)}')
print(f'Also Friend of: {", ".join(f for f in friends_to if f not in friends_from)}')
