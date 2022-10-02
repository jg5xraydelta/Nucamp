def display(deck, plyr0, plyr1):
    # deck passes the deck attributes, plyr0 is the computer, plyr1 is the human player
    print("----------------------------------------------------")
    print(plyr0.name, "Stock pile:", plyr0.stock[-1])
    print(plyr0.name, "Hand:", plyr0.hand)
    print(plyr0.name, "Discard piles:", plyr0.top_discards())
    print("----------------------------------------------------")
    print("Build piles:", [i[-1] for i in list(deck.build.values())])
    print("----------------------------------------------------")
    print(plyr1.name, "Stock pile:", plyr1.stock[-1])
    print(plyr1.name, "Hand:", plyr1.hand)
    print(plyr1.name, "Discard piles:", plyr1.top_discards())
    print("----------------------------------------------------\n")
