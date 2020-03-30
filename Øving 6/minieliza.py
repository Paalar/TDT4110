from random import randint

def pick_sentence(sentences):
    return sentences[randint(0, len(sentences) -1)]

def print_sentence(sentence1, sentence2, sentence3):
    print(sentence1, sentence2+sentence3)

def intro_text():
    print("Hei, jeg heter Eliza og vil gjerne snakke med deg.\nIkke start svar med stor bokstav og bruk hele setninger.\nSkrive 'hade' hvis du vil avslutte samtalen")


def main():
    questions = ["Hva gjør du", "Hvordan går det", "Hvorfor heter du", "Liker du å hete", "Føler du deg bra", "Hva har du fjort idag", "Hva tenker du om framtiden", "Hva gjør deg glad", "Hva gjør deg trist"]
    follow_ups = ["Hvorfor sier du", "Hva mener du med", "Hvor lenge har du sagt", "Hvilke tanker har du om", "Kan du si litt mer om", "Når tenkte du første gang på"]
    respones = ["Fint du sier det", "Det skjønner jeg godt", "Så dumt da", "Føler meg også sånn", "Blir trist av det du sier", "Så bra", "Du er jammen frekk"]

    intro_text()
    name = input("Hva er navnet ditt?   ")

    while True:
        print_sentence(pick_sentence(questions), name, "?")
        answer = input("Svar:    ")
        if answer == "hade":
            print_sentence(pick_sentence(respones), name, ".")
            break

        print_sentence(pick_sentence(follow_ups), answer, "?")
        print(input("Svar:       "))
#        if answer == "hade":
#            print_sentence(pick_sentence(respones), name, ".")
#            break

        print_sentence(pick_sentence(respones), name, ".")


main()
