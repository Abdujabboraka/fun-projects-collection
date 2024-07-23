d = {'number1':9, 'number2':-8, 'number3':7 , 'number4':-6, 'number5':100}
d1 ={}
def iner():
    for i in d:
        if d[i] > 0:
            d1[i] = d[i]
    print(d1)
iner()