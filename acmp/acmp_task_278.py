s = input()
t = input()

i = 0
j = 0

while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1

print("YES" if i == len(s) else "NO")