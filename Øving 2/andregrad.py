import math

print("Nå skal vi løse andregradsligninger, huff.")

a = int(input("Hva er tallet a?\n"))
b = int(input("Hva er tallet b?\n"))
c = int(input("Hva er tallet c?\n"))

d = ((b**2) - 4*a*c)
if d >= 0:
    x = (b*(math.sqrt(d))/(2*a))

if d < 0:
    print("Andregradsligningen {0}x^2 + {1}x + {2} = 0\nTallet er imaginært".format(a, b, c))
elif d > 0:
    print("Andregradsligningen {0}x^2 + {1}x + {2} = 0\nTallet er reelt med to løsninger".format(a, b, c, x))
elif d == 0:
    print("Andregradsligningen {0}x^2 + {1}x + {2} = 0\nTallet er reelt, med ett svar {3}".format(a, b, c, x))
