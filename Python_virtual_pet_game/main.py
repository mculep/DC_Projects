############

from pet import Pet, CuddlyPet
from toy import Toy

######################## INTRODUCTION TO GAME ########################

name = input("Please enter your name: ")
print(f"\nAloha, {name.capitalize()}! Welcome to the Dog Pound!\n")

pets = []

############################ MAIN MENUS ############################

# ----- Main menu which is the intro menu to adopt a dog-----

main_menu = [   
    "Enter 1 to adopt a dog:\n",
]
# I created a sub-menu so "Adopt a dog" would not be on the main list of things to do with your new dog. I want
# player to have only one dog.

second_menu = [   
    
    "Play with your dog",
    "Cuddle with your dog",
    "Give your dog some snacks",
    "See what your dog needs",
    "Give a toy to your dog",
    "Ignore your dog all day",
    "Abandon your dog and leave the game\n"
]

adoption_menu = [
    "Non-Cuddly dog, but still a good and smart dog",
    "A Cuddly dog\n"
]



######################## ERROR FUNTIONS / CHOICE FUNCTIONS #######################


def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")    

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += ""
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice


######################## ADOPTION MENU WITH ADOPTION FUNCTIONS #######################


# This function loops to the main menu choice above
# When player clicks on 1 to adopt a new pet. It then goes ahead to ask player a couple questions. 
# It is also appending from Cuddlypet in the pet.py

def main():    
    while True:
        choice = get_user_choice(main_menu)
        if choice == 1:
            pet_name = input("What would you like to name your dog?\n")
            print("Please choose the type of dog:\n")
            type_choice = get_user_choice(adoption_menu)
        
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            print("Congrats on your adoption! Now pick what you want to do with your new dog.\n")
            break


# I created another method to grab the values from  "second_menu" and goes through th list of choices above
# This acts like a sub - menu.

def main_2():    
    while True:    
        choice = get_user_choice(second_menu)
        if choice == 1:
            for pet in pets:
                pet.get_love()

        elif choice == 2:
            for pet in pets:
                pet.get_love()

        elif choice == 3:
            for pet in pets:
                pet.eat_food()

        elif choice == 4:
            for pet in pets:
                print(pet)

        elif choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
                
        elif choice == 6:
            # Pet levels naturally lower.
            for pet in pets:
                pet.be_alive()

        elif choice == 7:
            print("You're evil for abandoning your dog\n")
            break
            

# Calling the funtions 

main()
main_2()


########################################################################





