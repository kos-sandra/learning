def is_dvoyakoe(x):
    x = str(x)
    x = set(x)
    if len(x) < 3:
        return False
    return True

n = int(input())
smoller = n
bigger = n

while is_dvoyakoe(smoller):
    smoller -= 1

while is_dvoyakoe(bigger):
    bigger += 1
    if n - smoller < bigger - n:
        break


print(smoller if n - smoller <= bigger - n else bigger)