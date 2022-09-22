# Week Two High Level Game Algo Submission:
1 Create deck generator.

2 Pick first player using randint.

3 Create player dictionary for hand and 4 discard piles.

4 Create a build_pile dictionary that contains 4 key/value pairs.  Each value is an empty list.

5 Create functions for play_build, draw_card, play_hand, and discard.

6 Create displayed_card list for each player and build pile and draw_pile.

7 Each turn displays all displayed_card lists and option list for the functions in step 5.

8 Player chooses a play and game must check that each successive number is either a wild card or the next integer.

9 Turn ends once player has chosen to discard.  Next player refills hand to a length of 5 from the draw_pile.

10 Game ends when any player build_pile has a length of zero.

--------------------------------------------------------------------------------------------------------------------

# Game Rules/Procedure
# shuffle the deck

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
--------------------------------------------------------------------------------------------------------------------