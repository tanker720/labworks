import math
c =  int(input('0<=x<= 360: '))
x = math.radians(c)
def t(x):
    y = math.sin(x)**2                   
    a = math.sqrt(1-y)
    print (a)
t(x)


