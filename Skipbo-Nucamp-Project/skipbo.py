import random as r

class deck:
    deck_iter = generate_deck_iter()
    top_deck = next(deck_iter)
    build = {"b1":[],"b2":[],"b3":[],"b4":[]}

    def generate_deck_iter(self, bx = ''):
        deck_list = []
        if bx == '':
            for i in range(1,12):
                deck_list.extend([str(i)]*12)
            deck_list.extend(['SKB']*12)
        else:
            for i in self.deck_iter:
                deck_list.append(i)
            for i in range(1,12):
                deck_list.extend([str(i)])

        r.shuffle(deck_list)
        deck_iter = iter(deck_list)
        return deck_iter

    def deal(self, player):
        while len(player.stock) < 5:
            player.hand.append(next(deck_iter))
        pass

# shuffle the deck (144 cards numbered 1-12)(twelve 1's, twelve 2's,..., twelve 12's)(18 skipbo cards)
class player:
    hand = []
    stock = []
    discard = {"d1":[],"d2":[],"d3":[],"d4":[]}
    top_dcards = [self.discard["d1"][-1],self.discard["d2"][-1],self.discard["d3"][-1],self.discard["d4"][-1]]

    def __init__(self):
        self.name = input("Please choose your player name:")

    def generate_stock(self):
        while len(self.stock) < 30:
            self.stock.append(next(deck_iter))

    def play_build(self, card):
        # play a card from your hand, top_draw_card, or discard pile

        pass

    def draw(self):
        while len(self.hand) < 5:
            self.hand.append(next(deck_iter))

    def discard(self):
        # discard one card from hand to end your turn
        pass


        











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

