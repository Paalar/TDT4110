
def func1(a):
    import random
    x = [0 for i in range(a)]
    print (x)

    for i in range(a):
        x[i] = random.randint(0,10)

    return x

def func2(x):
    return sorted(x)

# funksjon1
#

tall = int(input("Skriv inn et tall: "))
k = func1(tall)
y = func2(k)
print(y)
