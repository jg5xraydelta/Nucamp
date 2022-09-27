def display(dk, plyr0, plyr1):
    # dk passes the deck attributes, plyr0 is the computer, plyr1 is the human player
    print("----------------------------------------------------")
    print("Draw pile:", dk.top_deck)
    print("Build piles:", dk.build)
    print("----------------------------------------------------")
    print(plyr1.name, "Stock pile:", plyr0.stock[-1])
    print(plyr1.name, "Discard piles:", plyr0.top_dcard)
    print("----------------------------------------------------")
    print(plyr2.name, "Stock pile:", plyr1.stock[-1])
    print(plyr2.name, "Hand:", plyr1.hand)
    print(plyr2.name, "Discard piles:", plyr1.top_dcard)
    print("----------------------------------------------------/n")


