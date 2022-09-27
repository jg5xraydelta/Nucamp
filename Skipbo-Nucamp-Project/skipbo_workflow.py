import skipbo as skb


while True:
    # Prompt player name and ask if they would like to play.
    player_name = input("What is your name?")
    print("Would you like to play a game", player_name + "?")
    print("Don worry ", player_name, " the game is called skipbo!")
    response = input("Yes or No?")

    if response in ["No", "no", , "N", "n"]:
        print("Goodbye!")
        break

    # Choose which player goes first.
    num = input("Let's see who goes first", player_name, "Pick a number from 1 to 10...")
    player_control = 0

    if num%2 == 0:
        print(player_name, "goes first!")
        player_control = 1
    else:
        print("Mr. Computer goes first... womp, womp, wooomp")

    # Generate the deck
    dek = skb.generate_deck_iter()

    













