def is_palindrome(s):
    s1 = s[:len(s)//2]
    s2 = s[len(s)-1:len(s)-1-len(s)//2:-1]
    return s1==s2




s = input()
if len(set(s)) < 2:
    print("NO SOLUTION")
elif is_palindrome(s):
    print(s[:len(s) - 1])
else:
    print(s)

