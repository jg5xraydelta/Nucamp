import skipbo_mods

""" build = {"b1": ['1', '2'], "b2": ['3', '4'],
         "b3": ['5', '6'], "b4": ['7', '8']}
card = [int(max(i)) + 1 for i in list(build.values())]

#print(list(build.values()))
print([i[-1] for i in list(build.values())]) """

"""hand = [1,2,3]

discards = [10,12]

discards.remove(12)

print(discards)"""

""" a = skipbo.player("a")

a.hand = ['1','2','3','4']

print(a.top_discards())
print(a.discard_pile)

a.discard('4','d3')

print(a.top_discards())
print(a.discard_pile) """

""" list = []
print(list[-1]) """

while True:
        print(game_display.display(deck, player0, player1))
        print("Enter 'discard' if you would like to discard.")

        
        pile = input("Which pile would you like to play? Enter s, h or d:").lower()
        if pile in ['discard','']:
            break

        card = input("Which card would you like to play? Enter 1-12 or skb:").lower()
        if card == ['discard','']:
            break
                
        cards = deck.playable_cards()

        # Double check that player has the card
        while card not in [*self.hand, *self.top_discards(), self.stock[-1], cards]:
            card = input(
                "Card must come from your hand, discard piles or stock pile and be playable.")
            if card == "cancel":
                break

        # find locations of cards to be played and build pile destination
        if self.name == 'mrComputer':
            # card located by hiarchy stock, hand, discard
            pile = self.card_pile(card)

        if card == 'skb':
            bx = "b" + str(r.randint(1, 4))
        else:
            bx = "b" + str(cards.index(card))

        deck.build[bx].append(card)

        if pile == 's':
            self.stock.remove(card)
        elif pile == 'h':
            self.hand.remove(card)
        elif pile == 'd':
            dx = "d" + str(self.top_discards().index(card) + 1)
            self.discard_pile[dx].remove(card)

