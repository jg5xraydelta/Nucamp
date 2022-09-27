def display(dk, plyr1, plyr2):
    print("----------------------------------------------------")
    print("Draw pile:", dk.top_deck)
    print("Build piles:", dk.build)
    print("----------------------------------------------------")
    print(plyr1.name, "Stock pile:", plyr1.stock[-1])
    print(plyr1.name, "Hand:", plyr1.hand)
    print(plyr1.name, "Discard piles:", plyr1.top_dcard)
    print("----------------------------------------------------")
    print(plyr2.name, "Stock pile:", plyr2.stock[-1])
    print(plyr2.name, "Hand:", plyr2.hand)
    print(plyr2.name, "Discard piles:", plyr2.top_dcard)
    print("----------------------------------------------------/n")


