def input_point():
    array = [int(x) for x in input().split(' ')]
    x1 = array[0]
    y1 = array[1]
    x2 = array[2]
    y2 = array[3]
    x1,x2 = min(x1,x2), max(x1,x2)
    y1,y2 = min(y1,y2), max(y1,y2)
    res = {'x1': x1,'y1': y1,'x2': x2,'y2': y2, 'in': [0,0,0,0]}
    return res


def check_areas_in(array,target):
    w = max(0, min(target['x2'], array['x2']) - max(target['x1'], array['x1']))
    h = max(0, min(target['y2'], array['y2']) - max(target['y1'], array['y1']))
    s = w*h
    return [w,h,s]


n = int(input())
areas = {}

for i in range(n):
    areas[i] = input_point()

coordinates_target = input_point()

total = 0
for i in range(n):
    total += check_areas_in(areas[i],coordinates_target)[2]

print(total)



