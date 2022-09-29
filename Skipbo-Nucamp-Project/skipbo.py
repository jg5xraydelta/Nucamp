import random as r
import game_dispay as gd


class deck:
    build = {"b1": [], "b2": [], "b3": [], "b4": []}
    cards = [int(i[-1]) + 1 for i in build.values()]

    def generate_deck_iter(self, dk=[], bx=''):
        # dk is the current deck during game play; bx is a key for the build dictionary above
        deck_list = []
        if bx == '':
            for i in range(1, 12):
                deck_list.extend([str(i)]*12)
            deck_list.extend(['SKB']*12)
        else:
            for i in dk:
                deck_list.append(i)
            for i in range(1, 12):
                deck_list.extend([str(i)])

        r.shuffle(deck_list)
        dk = iter(deck_list)
        return dk


class player:
    discard_pile = {"d1": [''], "d2": [''], "d3": [''], "d4": ['']}

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stock = []
        self.discards = [self.discard_pile["d1"][-1], self.discard_pile["d2"]
                           [-1], self.discard_pile["d3"][-1], self.discard_pile["d4"][-1]]

    def generate_stock(self, dk):
        """
        self (object) is either player0 or player1 
        dk (string) will be the current deck generator

        """
        while len(self.stock) < 30:
            self.stock.append(next(dk))

    def card_pile(self, card):
        if card in self.stock[-1]:
            return 's'
        if card in self.hand:
            return 'h'
        if card in self.top_dcards:
            return  'd'



    def draw(self, dk):
        """
        self (object) is either player0 or player1
        dk (iterator) will be the current deck generator

        """
        while len(self.hand) < 5:
            self.hand.append(next(dk))

    def play_build(self, card, dk):
        """
        self (object) is either player0 or player1
        card (string) will be a number from 1-12 string type or skb
        pile (string) will indicate whether the card comes from stock, hand, discard pile
        dk (string) will be the current deck generator
        dx (string) will be the key of the discard pile (there are 4 total)
        bx (string) will be the key of the build pile that will have card added
        """
        while card not in [self.hand, self.top_dcards, self.stock[-1]]:
            card = input(
                "Card must come from your hand, discard piles or stock pile.")
            if card == "cancel":
                break
                
        # find locations of cards to be played and build pile destination
        if self.name == 'mrComputer': 
            pile = self.card_pile(card)

        bx = "b" + str(dk.cards.loc(card)+1)
        if pile == 'd':
            dx = "d" + str(self.discards.loc(card) + 1)

        dk.build[bx].append(card)

        if pile == 's':
            self.stock.pop(card)
        elif pile == 'h':
            self.hand.pop(card)
        elif pile == 'd':
            self.discard[dx].pop(card)

    def discard(self, card, dx):
        """
        self is either player0 or player1
        card will be a number from 1-12 string type or skb
        dx will be the key of the discard pile (there are 4 total)
        """
        while card not in self.hand:
            card = input("Card must come from your hand.")
            if card == "cancel":
                break

        self.discard_pile[dx].append(card)
        self.hand.pop(card)

# player that draws highest card goes first/dealer

# dealer deals 30 cards to each player; this creates the stock_pile

# draw_pile (community)
# build_pile ---> (community) "around" draw pile
#            ---> must be in ascending order; skipbo card is wild; 1-12 complete pile
#            ---> must begin with skipbo or 1

# player board: 4 discard piles, 1 stock pile
# discard_pile ---> (unique to player) can be built in any order; last in first out
# stock_pile (goal of game = no cards)(unique to player) ---> top card facing up; top card is the only card showing
#                                      ---> can only play card showing; can't look at others
# hand: player sees all card in hand; only 5 to start turn

# playing a card implies that the player has placed a card in the build pile
# cards can be played from discard or stock or hand
# play priority: stock - hand - discard

# turn 1: first player draws 5 cards from draw_pile; play all 5 cards and you may draw 5 more
# play ends when player discards one card in discard pile
# cards left in hand are kept

# turn 2: player draws cards to complete 5-card-hand and then tries to play
