def display(deck, plyr0, plyr1):
    # dk passes the deck attributes, plyr0 is the computer, plyr1 is the human player
    print("----------------------------------------------------")
    print("Build piles:", deck.build.values())
    print("----------------------------------------------------")
    print(plyr0.name, "Stock pile:", plyr0.stock[-1])
    print(plyr0.name, "Discard piles:", plyr0.discards)
    print("----------------------------------------------------")
    print(plyr1.name, "Stock pile:", plyr1.stock[-1])
    print(plyr1.name, "Hand:", plyr1.hand)
    print(plyr1.name, "Discard piles:", plyr1.discards)
    print("----------------------------------------------------\n")
