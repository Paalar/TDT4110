
birthdays = {
"22 nov": ["Lars", "Mathias"],
"10 des": " Elle ",
"30 okt": ["Veronica", "Rune"],
"12 jan": "Silje",
"31 okt": "Willy",
"8 jul": ["Brage", "Øystein"],
"1 mar": "Nina"
}

#add_birthday_to_date ("12 jan", "Sindre")

def add_birthday_to_date(date, name):
    onenamedate = []
    try:
        birthdays[date].append(name)
    except AttributeError:
        for i in birthdays[date]:
            onenamedate.append(i)
        birthdays[date] = []
        birthdays[date].append(name)
        birthdays[date].append("".join(onenamedate))
    except KeyError:
        birthdays[date] = []
        birthdays[date].append(name)

print("Når du er ferdig, skriv 'ferdig'")
while True:
    bursdagsbarn = input("Hvem har bursdag?")
    if bursdagsbarn.lower() == "ferdig":
        break
    bursdag = input("Når har personen bursdag?")
    if bursdag.lower() == "ferdig":
        break
    add_birthday_to_date(bursdag, bursdagsbarn)

print(birthdays)
