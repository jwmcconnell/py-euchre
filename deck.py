import random
from card import Card, Bower

class Deck:

  def __init__(self):
    self.cards = []
    self.fill_deck()
    self.shuffle_deck()

  def fill_deck(self):
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = [9, 10, 11, 12, 13, 14]
    for suit in suits:
      for value in values:
        if value == 11:
          self.cards.append(Bower(suit, value))
        else:
          self.cards.append(Card(suit, value))

  def shuffle_deck(self):
    random.shuffle(self.cards)

  def print_deck(self):
    for card in self.cards:
      card.print_card()