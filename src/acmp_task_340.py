# A1, B1, C1 = input().split()
# A2, B2, C2 = input().split()
# A1, B1, C1 = int(A1), int(B1), int(C1)
# A2, B2, C2 = int(A2), int(B2), int(C2)
# box1 = [A1, B1, C1]
# box2 = [A2, B2, C2]
# box1.sort()
# box2.sort()
# if box1 == box2:
#     print("Boxes are equal")
# elif box1[0] >= box2[0] and box1[1] >= box2[1] and box1[2] >= box2[2]:
#     print("The first box is larger than the second one")
# elif box1[0] <= box2[0] and box1[1] <= box2[1] and box1[2] <= box2[2]:
#     print("The first box is smaller than the second one")
# else:
#     print("Boxes are incomparable")

A1, B1, C1 = input().split()
A2, B2, C2 = input().split()
A1, B1, C1 = int(A1), int(B1), int(C1)
A2, B2, C2 = int(A2), int(B2), int(C2)
box1 = [A1, B1, C1]
box2 = [A2, B2, C2]
box1.sort()
box2.sort()
if box1 == box2:
    print("Boxes are equal")
# all - функция от генератора. проверяет, выполнены ли все условия внутри скобок
elif all(box1[i] >= box2[i] for i in range(3)):
    print("The first box is larger than the second one")
elif all(box1[i] <= box2[i] for i in range(3)):
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")