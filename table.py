from deck import Deck
from player import Player

class Table: 

  def __init__(self):
    self.players = self.setup_players()
    self.deck = Deck()
    self.kitty = []
    self.deal_cards()
  
  def setup_players(self):
    return [Player(x) for x in range(4)]

  def deal_cards(self):
    self.deck.shuffle_deck()
    i = 0
    for player in self.players:
      player.hand.add_cards(self.deck.cards[i:i + 5])
      i += 5
    self.kitty = self.deck.cards[20:]
    self.display_table()

  def display_table(self):
    for player in self.players:
      player.display_player_info()
    print("Top Card from Kitty:")
    self.kitty[0].print_card()