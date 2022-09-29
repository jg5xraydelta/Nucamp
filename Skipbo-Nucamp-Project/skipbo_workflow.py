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

        # mrComputer's turn
        while player_control == 0:
            
            # mrComputer's algo:
            while card in [player0.hand, player0.stock[-1]]

        # player1's turn
        while player_control == 1:



"""Mr. Computer algo/priority: play stock, hand, discard"""
    













