import random

mySum = 0
num = 0
while num < 100:
    num += 1
    mySum += num
print("Summen av de {0} første tallene er lik {1}".format(num, mySum))

x = 1
n = 1
while x <= 1000:
    x *= n
    n += 1
print("De {0} første tallene multiplisert sammen er lik {1}".format(n, x))

a = random.randint(1,10)
b = random.randint(1,10)
c = float(input("Hva er {0} ganger {1}?\n".format(a, b)))

while c != a*b:
    c = float(input("Dette er ikke riktig! Hva er {0} ganger {1}?\n".format(a, b)))

print("Dette var riktig, grættis!")
