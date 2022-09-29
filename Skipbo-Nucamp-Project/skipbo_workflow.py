import skipbo as skb
import game_display as game

while True:
    # Prompt player name and ask if they would like to play.
    player1 = input("What is your name?")
    player1 = skb.player(player1)

    # initiate computer player
    player0 = skb.player("mrComputer")

    print("Would you like to play a game", player1.name + "?")
    print("Don worry ", player1.name, " the game is called skipbo!")
    response = input("Yes or No?")

    if response in ["No", "no", "N", "n"]:
        print("Goodbye!")
        break

    # Choose which player goes first.
    num = input("Let's see who goes first", player1.name, "Pick a number from 1 to 10...")
    player_control = 0

    if num%2 == 0:
        print(player1.name, "goes first!")
        player_control = 1
    else:
        print(player0.name, "goes first... womp, womp, wooomp")

    # Generate the deck and each players stock pile
    dk = skb.generate_deck_iter()
    player0.generate_stock()
    player1.generate_stock()
    print("Deck has been shuffled.  Players have been dealt 30 cards each for their stock pile.")

    # player wins when all stock cards have been played
    while len(player0.stock) > 0 and len(player1.stock) > 0:

        # mrComputer's turn ---------------------------------------------------
        while player_control == 0:

            # mrComputer needs refill hand
            player0.draw(dk)
            
            # a list of possible plays needs to be generated with a function
            for card in dk.cards:

                # mrComputer's algo:
                while card in [player0.stock[-1], player0.hand, player0.top_dcards]
                    player0.play_build(card, dk)
                    break

                while card not in [player0.stock[-1], player0.hand, player0.top_dcards]
                    player0.discard()
                    player_control = 1
                    break

        # player1's turn -----------------------------------------------------
        while player_control == 1:
            player1.draw(dk)
            print(game.display(dk, player0, player1))
            
            # can you like to play build?
            card = ''            
            while card == '':
                pile = input("Which pile would you like to play? Enter s, h or d:").lower()
                if pile = 'discard':
                    break

                card = input("Which card would you like to play? Enter 1-12 or skb:").lower()
                if card = 'discard':
                    break
                
                player1.play_build(card, dk, pile)
            

            
            card = input("Which card would you like to discard? Enter 1-12 or skb:").lower()
            dx = "d" + input("Which discard pile do you want to put it in? Enter 1-4:")
            player1.discard(card, dx)
            player_control = 0

    if len(player0.stock) == 0:
        print("mrComputer wins!")
    else:
        print(player1.name, "wins!  Congratulations!!")

    play_again = input("Would you like to play again? Enter n for no:")
    if play_again == 'n':
        break

    


            



"""Mr. Computer algo/priority: play stock, hand, discard"""
    













