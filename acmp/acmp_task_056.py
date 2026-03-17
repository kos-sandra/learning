n = int(input())
friends_from = [input() for _ in range(n)]

m = int(input())
friends_to = [input() for _ in range(m)]


friends_from.sort()
friends_to.sort()
print(f'Friends: {", ".join(friends_from)}')
print(f'Mutual Friends: {", ".join(f for f in friends_to if f in friends_from)}')
print(f'Also Friend of: {", ".join(f for f in friends_to if f not in friends_from)}')
