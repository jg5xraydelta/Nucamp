import random

high_score = 0

def dice_game():
    global high_score
    while True:
        print("Current high score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")
       
        if choice == '1':
            print("\n")
            a, b = (random.randint(1,6),random.randint(1,6))
            print("You rolled a...", a)
            print("You rolled a...", b,"\n")
            print("You have rolled a total of:", a+b,"\n")
            if a+b > high_score:
                high_score = a+b
                print("New high score!\n")
        else:
            print("Goodbye!")
            break

dice_game()