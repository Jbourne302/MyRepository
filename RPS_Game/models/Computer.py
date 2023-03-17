from .Base import Player

class Computer(Player):

    def __init__(self, name: str) -> None:
        super().__init__(name) # initializes parent class (Player)
