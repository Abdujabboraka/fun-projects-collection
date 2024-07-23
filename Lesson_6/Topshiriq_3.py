import abc

d = {}
alifbo = sorted("qwertyuiopasdfghjklzxcvbnm")

def usul1():
    son = 1
    for i in alifbo:
        d[son] = i
        son += 1
    print(d)

def usul2():
    for i in alifbo:
        d[i] = None
    print(d)


# usul1()
# usul2()
