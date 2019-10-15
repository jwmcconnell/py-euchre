from hand import Hand

class Player:

  def __init__(self, position):
    self.position = position
    self.hand = Hand()

  def display_player_info(self):
    print('Player', self.position)
    self.hand.display_hand()