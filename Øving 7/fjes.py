streng = "given_name surname 10 gender relationship_status"

facebook = [["Pål", "Larsen", "20", "male", "single"], ["Pål", "Larsen", "21", "male", "single"], ["Pål", "Larsen", "22", "male", "single"],
["Pål", "Larsen", "23", "male", "single"], ["Per", "Larsen", "20", "male", "single"], ["Pål", "Jalapeno", "23", "male", "single"]]

def add_data(user):
    #user must be in the format given_name surname age gender relationship_status
    x = user.split(sep=" ")
    x[2] = int(x[2])
    return x

#Pål Larsen 20 Mann Singel
#print(add_data(streng))

def get_person(given_name, facebook):
    alike = []
    for i in range(len(facebook)):
        if facebook[i][0] == given_name:
            alike.append(facebook[i])
    return alike

#print(get_person("Pål", facebook))

def main():
    facebook = []
    while True:
        answer = input("Legg til en bruker. Må være formatert ved:\nFornavn Etternavn Alder Kjønn Forhold:\n")
        if answer == "done":
            Fornavn = input("Hvilket fornavn vil du søke etter?\n")
            folk = get_person(Fornavn, facebook)
            if len(get_person(Fornavn, facebook)) == 0:
                print("Ingen i denne listen har dette navnet.")
                return
            else:
                print("Det finnes {0} med navnet {1}.\nDe er:".format(len(folk), Fornavn))
                for i in range(len(folk)):
                    if folk[i][3].lower() == "male" or folk[i][3].lower() == "mann" or folk[i][3].lower() == "m":
                        print("\n{0} {1}, han er {2} år gammel, han er {3}".format(folk[i][0], folk[i][1], folk[i][2], folk[i][4]))

                    elif folk[i][3].lower() == "female" or folk[i][3].lower() == "kvinne" or folk[i][3].lower() == "k" or folk[i][3].lower() == "f":
                        print("\n{0} {1}, hun er {2} år gammel, hun er {3}".format(folk[i][0], folk[i][1], folk[i][2], folk[i][4]))
                    else:
                        print("Du suger")
                return
        user = add_data(answer)
        facebook.append(user)

print(main())
