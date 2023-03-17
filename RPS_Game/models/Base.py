class Player:

    def __init__(self, name: str) -> None:
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.name = name

    def won_round(self) -> None:
        self.wins += 1
        print(f"{self.name} won this round!\n")

    def lost_round(self) -> None:
        self.losses += 1
        print(f"{self.name} lost this round!\n")

    def tied_round(self) -> None:
        self.draws += 1
        print(f"This round was a draw!\n")
