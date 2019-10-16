from card import Card, Bower

class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def add_cards(self, cards):
        for card in cards:
            self.cards.append(card)

    def display_hand(self):
        print("Hand:", end="\n")
        for i, card in enumerate(self.cards):
            print(i, ": ", sep="", end="")
            card.print_card()
        print("")