def number_of_lines(filename):
    f = open(filename, "r")
    return(len(f.readlines()))

print("Det er", number_of_lines("numbers.txt"), "Linjer i filen")


def number_freqeuncy(filename):
    numbers = {}
    f = open(filename, "r")
    read = f.read()
    for i in read:
        occurence = 0
        try:
            numbers[int(i)] = []
            for j in read:
                if j == i:
                    occurence += 1
            numbers[int(i)].append(occurence)
        except ValueError:
            pass
    return numbers

numbers = number_freqeuncy("numbers.txt")

for i, j in numbers.items():
    print("Tallet {0} forekommer {1} ganger".format(i, j[0]))
