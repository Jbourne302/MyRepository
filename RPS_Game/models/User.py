from .Base import Player

class User(Player):

    def __init__(self, name: str, total_num_of_rounds: str) -> None:
        super().__init__(name)
        self.total_num_of_rounds = int(total_num_of_rounds)
        self.games_played = 0

    def played_round(self) -> None:
        self.games_played += 1
