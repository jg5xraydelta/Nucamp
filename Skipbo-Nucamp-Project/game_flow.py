from game_play import mrComputer, player1_prompt
import game_class
import random as r

while True:
    ################################################################# GAME SETUP
    # initiate mrComputer 
    player0 = game_class.player("mrComputer")
    player1 = input("What is your name?  ")
    player1 = game_class.player(player1)

    # Prompt player name and ask if they would like to play.
    print("Would you like to play a game", player1.name + "?")
    print("Don't worry ", player1.name, " the game is called... skipbo!")
    response = input("Yes or No? ")

    if response in ["No", "no", "N", "n"]:
        print("Goodbye!")
        break

    # Choose which player goes first.
    num_string = "Let's see who goes first " + player1.name + ". Pick a number from 1 to 10...  "
    num = input(num_string)
    player_control = 0

    if int(num)%2 == 0:
        print(player1.name, "goes first!")
        player_control = 1
    else:
        print(player0.name, "goes first... womp, womp, wooomp")

    # Generate the deck and each players stock pile
    deck = game_class.deck()
    dk = deck.generate_deck_iter()

    player0.generate_stock(dk)
    player1.generate_stock(dk)
    print("Deck has been shuffled.  Players have been dealt 30 cards each for their stock pile.")

    ################################################################# GAME PLAY
    # player wins when all stock cards have been played
    while len(player0.stock) > 0 and len(player1.stock) > 0:

        # mrComputer's turn ---------------------------------------------------
        while player_control == 0:

            # mrComputer needs to re/fill hand
            player0.draw(dk)

            # mrComputer checks for a play
            mrComputer(deck, dk, player0, player1)

            # check if stock pile is empty and mrComputer wins
            if len(player0.stock) == 0:
                break  

            # mrComputer discards
            dx = "d" + str(r.randint(1,4))
            card = player0.hand[r.randint(0,len(player0.hand)-1)]
            print("mrComputer is discarding...")
            player0.discard(card, dx)
            player_control = 1
        

        # player1's turn -----------------------------------------------------
        while player_control == 1:

            # player1 needs to re/fill hand
            player1.draw(dk)
            
            # player1 checks for a play
            player1_prompt(deck, dk, player0, player1)
                        
            # check if stock pile is empty and player1 wins
            if len(player1.stock) == 0:
                break

            # player1 discards
            card = input("Which card would you like to discard? Enter 1-12 or skb:").lower()
            dx = "d" + input("Which discard pile do you want to put it in? Enter 1-4:")
            print(player1.name, "is discarding...")
            player1.discard(card, dx)
            player_control = 0
        
        #----------------------------------------------------------------------

    ################################################################# GAME ENDING    
    # decide winner
    if len(player0.stock) == 0:
        print("mrComputer wins!")
    else:
        print(player1.name, "wins!  Congratulations!!")

    # prompts to play again
    play_again = input("Would you like to play again? Enter n for no:")
    if play_again == 'n':
        print("Goodbye", player1, ", thanks for playing!")
        break