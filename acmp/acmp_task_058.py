def input_matrix(x):
    result = []
    for i in range(x):
        array = [int(x) for x in input().split()]
        result.append(array)
    return result


def find_squares(matrix):
    if len(matrix) < 2:
        return True
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
                return False
    return True

general_n = int(input())

for n in range(general_n):
    x, m = [int(x) for x in input().split()]
    matrix = input_matrix(x)
    # print(stacked)
    print("YES" if find_squares(matrix) else "NO")
