from hand import Hand

class Player:

  def __init__(self, position):
    self.position = position
    self.hand = Hand()

  def display_player_info(self):
    print('Player', self.position)
    self.hand.display_hand()

  def trump_choice(self, pos_trump):
    self.hand.display_hand()
    print("Would you like", pos_trump.suit, "as trump?")
    while True:
      decision = input("[yes]/[no]: ")
      if decision == "yes" or decision == "y":
        return True
      elif decision == "no" or decision == "n":
        return False