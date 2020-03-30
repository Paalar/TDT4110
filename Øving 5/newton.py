import math
def f(x):
    fx = (x-12)*(math.e**(5*x)) - 8*((x + 2))**2
    return fx

def g(x):
    gx = (-x - 2*x**2 - 5*x**3 + 6*x**4)
    return gx

def fd(x):
    (f(x + h/2)- f(x - h/2))/2

def gd(x):
    (g(x +h/2) - f(x - h/2))/2

def newton(fd, f, x):
    for i in range(x):
        if fd == 0:
            return x
        x = x - f(x)/fd(x)
        return x


newton(fd(12), f(12), 12)
