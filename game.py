from table import Table

class Game: 

  def __init__(self):
    self.table = self.game_menu()

  def game_menu(self):
    print("Hi! Thank you for starting a game of py-euchre")
    print("euchre menu:")
    print("0: Start game")
    while True:
      val = input("Please pick an option: ")
      try:
        val = int(val)
      except ValueError:
        continue
      if val == 0:
        return Table()

if __name__ == "__main__":
  game = Game()