N = int(input())
days = []

for x in range(N):
    teachers = set()
    p = input().split()
    d_start = int(p[0])
    d_fin = int(p[1])
    for d in range(d_start, d_fin+1):
        teachers.add(d)
    days.append(teachers)

com = days[0]
for t in days:
    com = com & t
if len(com) > 0:
    print("YES")
else:
    print("NO")
