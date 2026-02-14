n = int(input())
m = int(input())

childrens = {
    "semolina": [],
    "oatmeal": [],
    "all": []
}

for nn in range(n):
    childrens["semolina"].append(input())

for mm in range(m):
    x = input()
    if x not in childrens["semolina"]:
        childrens["oatmeal"].append(x)
    else:
        index = childrens["semolina"].index(x)
        childrens["semolina"].pop(index)
        childrens["all"].append(x)

counter = len(childrens["all"])

print(counter) if counter > 0 else print("Таких нет")