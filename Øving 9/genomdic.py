my_family = {}

def add_family_member(role, name):
    for i in my_family:
        if i == role:
            my_family[role].append(name)
            return my_family
    my_family[role] = []
    my_family[role].append(name)
    return my_family

print("Når du er ferdig med å legge til navn, skriv ferdig.")
while True:
    navn  = input("Hva er navnet til familie medlemmet?\n")
    if navn.lower() == "ferdig":
        print(my_family)
        break
    rolle = input("Hva er rollen til dette familie medlemmet?\n")
    if rolle.lower() == "ferdig":
        print(my_family)
        break
    add_family_member(rolle, navn)
