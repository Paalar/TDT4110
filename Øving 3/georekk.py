n = float(input("N"))
r = 0.5
r0 = 0
while n >= 0:
    r0 += r**n
    n -= 1

print ("Summen av rekken er ", r0)

tol = float(input("\nen toleranseverdi"))

r0 = 0
n = 0
r = 1/2
while r0 <= (1/(1-r))-tol:
    r0 += r**n
    n += 1
print ("For å være innenfor toleranseverdien", tol, "kjørte løkken", n, "ganger.")
print ("Differanse mellom virkelig og estimert verdi er ", 2-r0)
