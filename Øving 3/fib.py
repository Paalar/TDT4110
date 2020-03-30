fiblsum = []
fibl = []
def fibonacci(k):
    fib1, fib2 = 0, 1
    for i in range(k):
        fib1, fib2 = fib2, fib1+fib2
        fiblsum.append(fib1)
        fibl.append(fib1)
    return fib1
    return sum(fiblsum)
    return fibl

k = int(input("Skriv in verdien til k der k er det k'te tallet i fibonaccisekvensen.\n"))
print("\n\n{1} er fibonaccitallet når k = {0}.\nSummen av {0} fibonaccitall er {2}.\nDette er en liste som inkluderer {0} fibonaccitall \n{3}".format(k, fibonacci(k), sum(fiblsum), fibl))
