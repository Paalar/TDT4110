from math import sin

print("Nå skal vi derivere sin(x) numerisk")
h = eval(input("Skriv inn høyde verdien \"h\".\n"))
x = eval(input("Nå skriv inn x variabelen.\n"))

f1 = sin(x)
f2 = sin(x + h)

print("sin(x)", "{:.4g}".format(f1))
print("sin(x + h) er", "{:.4g}".format(f2))
print("sin(x) derivert numerisk", "{:.10f}".format((f2-f1)/h))
