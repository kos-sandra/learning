# def from_digits_to_letters(n):
#     return chr(n + ord('A') - 10) if n > 9 else str(n)

def from_letter_to_digits(a):
    if a == ' ':
        return 27
    if a >= 'A':
        return ord(a) - ord('A') + 10
    if '0' <= a <= '9':
        return int(a)

# def to_cc(n,cc):
#     res = []
#     if n < 10:
#         return str(n)
#     if n == 27:
#         return ' '
#     while n > 0:
#         res.append(from_digits_to_letters(n % cc))
#         n //= cc
#     return ''.join(res[::-1])


# def coding(a, i):
#     code = ord(a) - ord('a') + 1 if a != ' ' else 27
#     return to_cc((code + i) % 27, 27)

def decoding(x,i):
    x = from_letter_to_digits(x)
    code = (x - i)%27 + ord('a')-1
    if code < ord('a'):
        return ' '
    return chr(code)

s = input()

for i in range(len(s)):
    x = decoding(s[i], i + 1)
    print(x, end='')