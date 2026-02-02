# u = input()
#
#
# def check(u):
#     if '-' not in u:
#         return False
#     else:
#         return True
#
#
# def knight(u):
#     a,b = u.split('-')
#     B = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
#     if a[0] not in B or b[0] not in B or int(a[1]) > 8 or int(b[1]) > 8:
#         return "ERROR"
#     else:
#         x1 = B[a[0]]
#         y1 = int(a[1])
#         x2 = B[b[0]]
#         y2 = int(b[1])
#         dx = x2-x1
#         dy = y1 - y2
#         if (abs(dx) == 1 and abs(dy) == 2) or (abs(dx) == 2 and abs(dy) == 1):
#             return "YES"
#         else:
#             return "NO"
#
#
#
# if check(u) is False:
#     print("ERROR")
# else:
#     print(knight(u))


def solve(s):
    tokens = s.split('-')
    if len(tokens) != 2 or len(tokens[0]) != 2 or len(tokens[1]) != 2:
        return 'ERROR'

    row1 = tokens[0][1]
    row2 = tokens[1][1]
    if row1 not in '12345678' or row2 not in '12345678':
        return 'ERROR'
    row1 = int(row1)
    row2 = int(row2)

    B = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    col1 = tokens[0][0]
    col2 = tokens[1][0]
    if col1 not in B or col2 not in B:
        return 'ERROR'
    col1 = B[col1]
    col2 = B[col2]

    diff_rows = abs(row1 - row2)
    diff_cols = abs(col1 - col2)
    if (diff_rows, diff_cols) == (1, 2) or (diff_rows, diff_cols) == (2, 1):
        return 'YES'
    else:
        return 'NO'


print(solve(input()))
