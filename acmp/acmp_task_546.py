n = int(input())

array = [x for x in range(1, n + 1)]

while len(array) % 4 != 0:
    array += [0]

p,z = 0, len(array)-1

for i in range(1, len(array) // 4 +1):
    for j in range(1, 3):
        if array[z] == array[p] == 0:
            continue
        print(i, j, array[z], array[p])
        array = array[::-1]
        p ,z = p+1, z-1

# print(array)
