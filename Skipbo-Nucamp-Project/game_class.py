import random as r

# THERE ARE TWO CLASSES IN THIS FILE

# DECK Class -------------------------------------------------------------------------------
class deck:
    def __init__(self):
        self.build = {"b1": ['0'], "b2": ['0'], "b3": ['0'], "b4": ['0']}

    def playable_cards(self):
        cards = ['skb']
        for bcards in list(self.build.values()):
            p_card = str(int(bcards[-1]) + 1)
            cards.append(p_card)

        return cards

    def check_completed_build(self):
        bx = False
        if '12' in list(self.build.values()):
            bx = list(self.build.keys())[list(self.build.values()).index('12')]
            return bx

    def generate_deck_iter(self, dk=[], bx='begin'):
        # dk is the current deck during game play; bx is a key for the build dictionary above
        deck_list = []
        if bx == 'begin':
            for i in range(1, 12):
                deck_list.extend([str(i)]*12)
            deck_list.extend(['skb']*12)
        else:
            for i in dk:
                deck_list.append(i)
            for i in range(1, 12):
                deck_list.extend([str(i)])
            deck.build[bx] = ['0']

        r.shuffle(deck_list)
        dk = iter(deck_list)
        return dk

# PLAYER Class -------------------------------------------------------------------------------
class player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stock = []
        self.discard_pile = {"d1": ['1'], "d2": ['2'], "d3": ['3'], "d4": ['4']}

    def top_discards(self):
        """
        only cards at the top of the discard pile can be played
        """
        discards = []
        for dx in ['d1', 'd2', 'd3', 'd4']:
            if self.discard_pile[dx] == []:
                discards.append('empty')
            else:
                discards.append(self.discard_pile[dx][-1])
        return discards

    def generate_stock(self, dk):
        """
        self (object) is either player0 or player1 
        dk (string) will be the current deck generator
        """
        while len(self.stock) < 30:
            self.stock.append(next(dk))

    def check_cards(self, list1, list2):
        """
        finds a playable card for mrComputer
        """
        for card in list1:
            if card in list2:
                return str(card)
        return False

    def card_pile(self, card):
        """
        finds pile that contains card
        """
        if card == self.stock[-1]:
            return 's'
        if card in self.hand:
            return 'h'
        if card in self.top_discards():
            return 'd'

    def draw(self, dk):
        """
        refills hand
        self (object) is either player0 or player1
        dk (iterator) will be the current deck generator

        """
        while len(self.hand) < 5:
            self.hand.append(next(dk))

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
        self.hand.remove(card)

    def play_build(self, deck, dk, card, pile):
        """
        removes card from player and adds to build pile
        self (object) is either player0 or player1
        card (string) will be a number from 1-12 string type or skb
        pile (string) will indicate whether the card comes from stock, hand, discard pile
        dk (string) will be the current deck generator
        dx (string) will be the key of the discard pile (there are 4 total)
        bx (string) will be the key of the build pile that will have card added
        """
        # find which cards are playable according to the build piles
        cards = deck.playable_cards()

        #--------------------------------------------------------------------
        # find locations of cards to be played and build pile destination

        if self.name == 'mrComputer': # mrComputer################mrComputer
            pile = self.card_pile(card)
            # skb must be treated as a special case since it is 'wild' and can be played anywhere
            if card == 'skb':
                bx = "b" + str(r.randint(1, 4))
            else:
                # automatically plays card on the correct build pile
                bx = "b" + str(int(cards.index(card)))

        else: # player1##############################################player1
            # skb must be treated as a special case since it is 'wild' and can be played anywhere
            if card == 'skb':
                bx = "b" + input("Which build pile would you like to play? Enter 1-4: ")
                while bx not in ['b1', 'b2', 'b3', 'b4']:
                    print("Invalid entry.  Try again...")
                    bx = "b" +  input(
                        "Which build pile would you like to play the skb? Enter 1-4: ")
            else:
                # automatically plays card on the correct build pile
                bx = "b" + str(int(cards.index(card)))
        #---------------------------------------------------------------------

        # add card to build pile and change it's value to a number
        if card == 'skb':
            card_num = int(deck.build[bx][-1])
            card_str = str(card_num + 1)
            deck.build[bx].append(card_str)
        else:
            deck.build[bx].append(card)

        # check for a build pile that ends in 12
        while deck.check_completed_build():
            bx = deck.check_completed_build()
            deck.generate_deck_iter(self, dk, bx)

        # remove card from stock, hand, discards
        if pile == 's':
            self.stock.pop(-1)
        elif pile == 'h':
            self.hand.remove(card)
        elif pile == 'd':
            dx = "d" + str(self.top_discards().index(card) + 1)
            self.discard_pile[dx].remove(card)
