# start = [int(x) for x in input().split()]
# finish = [int(x) for x in input().split()]
#
# hh = start[0]
# mm = start[1]
#
# total = 0
#
# while hh != finish[0] or mm != finish[1]:
#     if mm == 30:
#         total += 1
#     if mm == 0:
#         v = 12 if hh % 12 == 0 else hh % 12
#         total += v
#
#     mm += 1
#
#     if mm == 60:
#         mm = 0
#         hh += 1
#     if hh == 24:
#         hh = 0
#
# print(total)

# hh, mm = [int(x) for x in input().split()]
# finish_hh, finish_mm = [int(x) for x in input().split()]
#
#
# def is_ahead_of_finish(hh, mm, finish_hh, finish_mm):
#     return finish_hh < hh or finish_hh == hh and finish_mm < mm
#
#
# def update_time(hh, mm):
#     if mm < 30:
#         return hh, 30
#     else:
#         return hh + 1, 0
#
#
# if is_ahead_of_finish(hh, mm, finish_hh, finish_mm):
#     finish_hh += 24
#
# hh, mm = update_time(hh, mm)
#
# total = 0
#
# while not is_ahead_of_finish(hh, mm, finish_hh, finish_mm):
#     if mm == 30:
#         total += 1
#     else:
#         total += 12 if hh % 12 == 0 else hh % 12
#     hh, mm = update_time(hh, mm)
#
# print(total)

#-----------------------------------
start = [int(x) for x in input().split()]
finish = [int(x) for x in input().split()]

hh = start[0]
mm = start[1]

f_hh = finish[0]
f_mm = finish[1]
if f_hh > hh or f_hh == hh and f_mm > mm:
    period_h = f_hh - hh
else:
    period_h = f_hh + 24 - hh

total = 0

for h in range(hh+1,hh+period_h+1):
    if h % 12 == 0:
        total += 12
    else:
        total += h % 12

if mm < 30 < f_mm:
    total += 1
if f_mm < 30 < mm:
    total -= 1

total += period_h

print(total)
#--------------------------------------