##Формат ввода.
# В первых двух строках указывается количество детей, любящих манную и овсяную каши (NN и MM).
# Затем идут NN строк — фамилии детей, которые любят манную кашу, и MM строк с фамилиями детей, любящих овсяную кашу.
# Гарантируется, что в группе нет однофамильцев.

# 3
# 2
# Васильев
# Петров
# Васечкин
# Иванов
# Михайлов


import pandas as pd

def add_new_men(x, porridge_lovers, porridge):
    index = len(porridge_lovers["name"])
    if x in porridge_lovers["name"]:
        index = porridge_lovers["name"].index(x)

    if x not in porridge_lovers["name"]:
        porridge_lovers["name"].append(x)
        index = len(porridge_lovers["name"]) - 1
        porridge_lovers["semolina"].append(0)
        porridge_lovers["oatmeal"].append(0)

    porridge_lovers[porridge][index] = 1

def all_porridge_lovers(porridge_lovers):
    name = porridge_lovers["name"]
    semolina = porridge_lovers["semolina"]
    oatmeal = porridge_lovers["oatmeal"]
    result = []
    counter = 0
    for i in range(len(name)):
        if semolina[i] == oatmeal[i]:
            counter += 1
            result.append(name[i])
    print(*result,sep='\n')
    return counter


n = int(input())
m = int(input())

porridge_lovers = {
    "name": [],
    "semolina": [],
    "oatmeal": []
}

for i in range(n):
    add_new_men(input(), porridge_lovers, "semolina")

for i in range(m):
    add_new_men(input(), porridge_lovers, "oatmeal")


childrens = pd.DataFrame(porridge_lovers)
print(childrens)


c = all_porridge_lovers(porridge_lovers)
z = len(porridge_lovers["name"])
if c == 0:
    print("Никто не любит обе каши")
elif c == z:
    print("Все дети любят и манку и овсянку")
else:
    print(f"Любят обе каши {c} детей из {z}.")