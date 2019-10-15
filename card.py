class Card:

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def print_card(self):
    print(self.suit, self.value)
  
class Bower(Card):

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    self.offsuit = self.set_offsuit()

  def set_offsuit(self):
    if self.suit == "diamonds":
      return "hearts"
    elif self.suit == "hearts":
      return "diamonds"
    elif self.suit == "clubs":
      return "spades"
    else:
      return "clubs"