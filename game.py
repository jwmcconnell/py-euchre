from deck import Deck

class Game: 

  def __init__(self):
    self.game_menu()
    self.deck = Deck()

  def game_menu(self):
    print("Hi! Thank you for starting a game of py-euchre")
    return


if __name__ == "__main__":
  game = Game()