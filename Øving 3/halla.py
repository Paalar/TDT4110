from random import randint

options = ["R", "P", "S"]

computer_choice = randint(0, len(options)-1)
computer_choice_index = options[computer_choice]
print (computer_choice_index)
