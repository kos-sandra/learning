s = open('INPUT.TXT').read()

x = s.split()
a = int(x[0])
b = int(x[1])

open('OUTPUT.TXT', 'w').write(str(a + b))