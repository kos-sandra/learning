def find_letters(f):
    letters = {}
    for i in range(len(f)):
        if f[i] not in letters:
            letters[f[i]] = 1
        else:
            letters[f[i]] += 1
    return letters


def condition2(f, s):
    for i in range(len(f)):
        if f[i] == s[i]:
            return False
    return True


first, second = input().split()

if len(first) != len(second):
    print("NO")

if condition2(first, second) and find_letters(first) == find_letters(second):
    print("YES")
else:
    print("NO")

