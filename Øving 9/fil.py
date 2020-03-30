def write_to_file(data):
    f = open("myText.txt", "a")
    f.write(data)
    f.close()

def read_from_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    print(content)

def main():
    while True:
        fil = input("Vil du lese eller skrive til filen?")
        if fil.lower() == "done":
            break
        elif fil.lower() == "skrive":
            write_to_file(input("Hva vil du skrive i filen?"))
            print("Filen heter myText.txt")
        elif fil.lower() == "lese":
            read_from_file(input("Hva heter filen du vil lese av?"))
        else:
            print("Sorry mac, dette funker ikke")

main()
