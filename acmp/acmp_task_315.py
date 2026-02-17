s = input()

def is_correct(s):
    for x in s:
        if ('0' > x or x > '9') and ('A' > x or x > 'Z'):
            return False
    return True


def to_digit(x):
    if '0' <= x <= '9':
        return int(x)
    return ord(x) - ord('A') + 10


def solution(s):
    if is_correct(s):
        m = max(s)
        print(max(2,to_digit(m)+1))
    else:
        print(-1)

solution(s)