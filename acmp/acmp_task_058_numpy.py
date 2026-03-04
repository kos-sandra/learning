import numpy as np

def find_squares(matrixes):
    for m in range(len(matrixes)):
        for i in range(len(matrixes[m])):
            array = matrixes[m][i]
            if all(x % 4 == 0 for x in array):
                return False
    return True

def input_matrix(x):
    result = np.array([])
    for i in range(x):
        array = [int(x) for x in input().split()]
        if result.size == 0:
            result = np.array([array])
        else:
            result = np.vstack((result, array))
    return result

general_n = int(input())

for n in range(general_n):
    x, m = [int(x) for x in input().split()]
    matrix = input_matrix(x)
    stacked = np.stack([matrix[:-1,:-1], matrix[1:,1:],matrix[1:,:-1],matrix[:-1,1:]], -1)

    # print(stacked)
    print("YES" if find_squares(stacked) else "NO")
