for i in range (1,5):
    for x in range(1,5):
        y = i*x
        print(y)

print("\n\n")

for a in range (2, 101):
    for b in range (2, a):
        if a % b == 0:
            break
        else:
            pass
    else:
        print(a)
