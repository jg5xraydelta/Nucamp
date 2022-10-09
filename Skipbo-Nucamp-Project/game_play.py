import game_display

# mrComputers decision algo
def mrComputer(deck, dk, player0, player1):
    while player0.check_cards(deck.playable_cards(), [player0.stock[-1]] + player0.hand + player0.top_discards()):
        card = player0.check_cards(deck.playable_cards(), [player0.stock[-1]] + player0.hand + player0.top_discards())
        pile = player0.card_pile(card)

        game_display.display(deck, player0, player1)
        print(player0.name,": play",card, 'from', pile)
        player0.play_build(deck, dk, card, pile)

        if len(player0.hand) == 0:
            player0.draw(dk)


def player1_prompt(deck, dk, player0, player1):
    while True:
        print(game_display.display(deck, player0, player1))

        cards = deck.playable_cards()

        # Double check that player has the card
        card = 'x'
        while (card not in [*player1.hand, *player1.top_discards(), player1.stock[-1]]) and (card not in cards):
            print("Enter 'discard' if you would like to discard.")
            card = input("Which card would you like to play? Enter 1-12 or skb:").lower()
            if card == "discard":
                break

        if card == "discard":
            break

        # find the right pile to remove it from
        pile = 'x'
        while pile not in ['s','h','d']:
            print("Enter 'discard' if you would like to discard.")
            pile = input("Which pile would you like to play? Enter s, h or d:").lower()
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
            else:
                print('No such pile...')
                continue

        if pile == 'discard':
            break

        player1.play_build(deck, dk, card, pile)
        print(player1.name,": play",card, 'from', pile)

        if len(player1.hand) == 0:
            player1.draw(dk)
