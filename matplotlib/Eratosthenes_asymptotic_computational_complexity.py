import matplotlib.pyplot as plt
from math import log


def resheto(n):
    eratos = [1] * (n+1)
    eratos[0] = eratos[1] = 0

    result = 0

    for i in range(2, int(n**0.5)+1):
        operations = 0
        if eratos[i]:
            for j in range(i * i, len(eratos), i):
                eratos[j] = 0
                operations += 1
        result += operations

    return result


def draw(x,y):
    plt.plot(x, y)
    plt.title('оценка сложности решета Эратосфена')
    plt.xlabel('размер решета')
    plt.ylabel('коэфф сложности')
    plt.grid(True)
    plt.show()


def draw_multiple(x,ys):
    for i in range(len(ys)):
        plt.plot(x,ys[i], label=f'График {i}', linewidth=2)


    plt.title(f'оценка сложности решета Эратосфена')
    plt.grid(True)
    # plt.tight_layout()
    plt.show()

x, y1, y2 = [], [], []
i = 10000
while i < 10000001:
    x.append(i)
    # y1.append()
    y2.append((resheto(i)/i) / (log(log(i,4.9), 5)/0.63))
    i = int(i*1.5)

draw_multiple(x, [y2]) #соотношение коэффициента сложности на подстановочную формулу лог(лог(и))
