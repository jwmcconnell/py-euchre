from deck import Deck
from player import Player

class Table: 

  def __init__(self):
    self.players = self.setup_players()
    self.deck = Deck()
    self.kitty = [] # left over cards after dealing
    self.dealer = 0 
    self.leader = 1
    self.deal_cards()
  
  def setup_players(self):
    return [Player(x) for x in range(4)]

  def order_table(self):
    # returns the players in the correct order to play a card or pick trump
    order_table = self.players[self.leader:] + self.players[:self.leader]
    return order_table

  def deal_cards(self):
    self.deck.shuffle_deck()
    i = 0
    for player in self.players:
      player.hand.add_cards(self.deck.cards[i:i + 5])
      i += 5
    self.kitty = self.deck.cards[20:]
    self.display_table()
    self.pick_trump()

  def pick_trump(self):
    self.first_trump_choice()
      
  def first_trump_choice(self):
    ordered_table = self.order_table()
    for player in ordered_table:
      player.trump_choice(self.kitty[0])

  def display_table(self):
    for player in self.players:
      player.display_player_info()
    print("Top Card from Kitty:")
    self.kitty[0].print_card()
    print()