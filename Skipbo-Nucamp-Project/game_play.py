import game_display

# mrComputers decision algo
def mrComputer(deck, dk, player0, player1):
    """ 
    mrComputer doesn't try to block player1; mrC plays all cards that are playable
    """
    # compare playable cards to the cards in mrComputer's hand, stock, discard
    while player0.check_cards(deck.playable_cards(), [player0.stock[-1]] + player0.hand + player0.top_discards()):
        card = player0.check_cards(deck.playable_cards(), [player0.stock[-1]] + player0.hand + player0.top_discards())
        pile = player0.card_pile(card)
        
        # mrComputer makes a play and the result is displayed
        print(player0.name, ": play", card, 'from', pile, "---------------------\n")
        player0.play_build(deck, dk, card, pile)
        game_display.display(deck, player0, player1)

        # mrComputer must refill if their hand is empty
        if len(player0.hand) == 0:
            player0.draw(dk)


# prompt player1 choices
def player1_prompt(deck, dk, player0, player1):
    while True:

        # which cards are playable on the build piles
        cards = deck.playable_cards()

        # check that player has the card
        card = None
        while (card not in [*player1.hand, *player1.top_discards(), player1.stock[-1]]) and (card not in cards):
            print("Enter 'discard' if you would like to discard.")
            card = input("Which card would you like to play? Enter 1-12 or skb: ").lower()
            if card == "discard":
                break

        if card == "discard":
            break

        # find the right pile to remove card from
        pile = None
        while pile not in ['s','h','d']:
            print("Enter 'discard' if you would like to discard.")
            pile = input("Which pile would you like to play? Enter s, h or d: ").lower()
            if pile == 's' and card != player1.stock[-1]:
                print('Wrong pile...')
                continue
            elif pile == 'h' and card not in player1.hand:
                print('Wrong pile...')
                continue                
            elif pile == 'd' and card not in player1.top_discards():
                print('Wrong pile...')
                continue    
            elif pile == 'discard':
                break

        if pile == 'discard':
            break

        # player1 makes a play and the result is displayed
        player1.play_build(deck, dk, card, pile)
        print(player1.name,": play",card, 'from', pile, "---------------------\n")
        print(game_display.display(deck, player0, player1))

        # player1 must refill if their hand is empty
        if len(player1.hand) == 0:
            player1.draw(dk)
