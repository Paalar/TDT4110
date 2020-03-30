n = int(input("Skriv inn 'n'\n"))

xii = 0
for i in range(1, n+1):
    xi = (1/(i**2))
    xii += xi
print("Etter {0} iterasjoner, var x like {1}".format(n, xii))


tol = float(input("Sett en toleranseverdi\n"))
i = 1
xi = 1
xii = 0
while xi >= tol:
    xi = (1/(i**2))
    xii += xi
    i += 1
print ("Med toleranseverdi {0} ble summen lik {1}, den kjørte {2} ganger".format(tol, xii, i))
