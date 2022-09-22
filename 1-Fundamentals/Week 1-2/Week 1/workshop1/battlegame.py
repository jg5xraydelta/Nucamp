while True:
    while True:
        wizard = "Wizard"
        elf = "Elf"
        human = "Human"

        hp_wizard = 70
        hp_elf = 100
        hp_human = 150

        wizard_damage = 150
        elf_damage = 100
        human_damage = 20

        hp_dragon = 300
        dragon_damage = 50

        print('1) Wizard  2) Elf  3) Human  4) Orc  5) Exit')
        character = input('Choose your character:')

        if character == '1' or character.lower() == "wizard":
            character = "Wizard"
            my_hp = hp_wizard
            my_damage = wizard_damage
            break
        elif character == '2' or character.lower() == "elf":
            character = "Elf"
            my_hp = hp_elf
            my_damage = elf_damage
            break
        elif character == '3' or character.lower() == "human": 
            character = "Human"
            my_hp = hp_human
            my_damage = human_damage
            break
        elif character == '4' or character.lower() == "Orc":
            character = "Orc"
            my_hp = 1
            my_damage = 500
            break
        elif character == '5':
            break
        else:
            print("Unknown character")
            continue

    if character == '5':
        print("You have chosen to end the game!")
        quit()

    print("You have chosen to be a/an " + character + "!  " + "You have " + str(my_hp) + " hit points and " + str(my_damage) + " damage points!\n")

    while True:
        hp_dragon = hp_dragon - my_damage
        print("The", character, "damaged the Dragon!")
        print("The dragons hitpoints are now: " + str(hp_dragon) + "\n")

        if hp_dragon <= 0:
            print("The Dragon has lost the battle!")
            break
            

        my_hp = my_hp - dragon_damage
        print("The " + character + " has been damaged!")
        print("The " + character + "'s hitpoints are now: " + str(my_hp) + ".\n ")

        if my_hp <= 0:
            print("The " + character + " has lost the battle!")
            break
    
    
    print("Would you like to play again? Y or N")
    replay = input()
    if replay == "Y":
        continue
    else:
        break
            

