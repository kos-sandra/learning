
def convertion_to_the_number_system(x,k):
    res = []
    while x > 0:
        res.append(x % k)
        x //= k
    return res


def mult_array(array):
    total = 1
    for x in array:
        total *= x
    return total


n,k = [int(x) for x in input().split()]
array = convertion_to_the_number_system(n,k)
print(mult_array(array) - sum(array))