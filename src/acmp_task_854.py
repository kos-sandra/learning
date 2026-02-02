g = input().split()
t1, t2 = int(g[0]), int(g[1])
m = input()
if m == 'freeze':
    print(min(t1,t2))
if m == 'heat':
    print(max(t1,t2))
if m == 'auto':
    print(t2)
if m == 'fan':
    print(t1)
    
# s = input().split( )
# sa = input()
# for x in s:
#     Tr = int(s[0])
#     Tc = int(s[1])
# if Tr > Tc:
#     if (sa == 'freeze') or (sa == 'auto'):
#         print(Tc)
#     else:
#         print(Tr)
# elif Tr < Tc:
#     if (sa == 'heat') or (sa == 'auto'):
#         print(Tc)
#     else:
#         print(Tr)
# else:
#     print(Tc)