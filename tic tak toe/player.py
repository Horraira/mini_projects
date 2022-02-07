import math
import random

# base class
class Player:
    # iniatialize it with the letter the player is
    # going to represent
    # __init__ is constructor function for python
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass