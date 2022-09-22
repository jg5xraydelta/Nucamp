import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input("Press enter to pick a card, or Q then enter to quit:")
    if choice.upper == 'Q':
        break

    card_index = random.randint(0,len(diamonds)-1)
    hand.append(diamonds[card_index])
    del diamonds[card_index]

    print("Hand:", hand)
    print("Diamonds:", diamonds)

    if not diamonds:
        print("There are no more cards to pick.")