from typing import Optional
from random import randint


## globals

CHOICES = { ## this is a dictionary
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors"
}

''' ------------ INTERFACES ------------ '''

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

class Computer(Player):

    def __init__(self, name: str) -> None:
        super().__init__(name) # initializes parent class (Player)

class User(Player):

    def __init__(self, name: str, total_num_of_rounds: str) -> None:
        super().__init__(name)
        self.total_num_of_rounds = int(total_num_of_rounds)
        self.games_played = 0

    def played_round(self) -> None:
        self.games_played += 1

def is_even(num: str) -> bool:
    return int(num)%2 == 0

''' ------------ VALIDATION FUNCTIONS ------------ '''

def get_num_of_games() -> str:

    num_of_games = input("How many games do you want to play?: ")

    num_is_even = is_even(num_of_games)
    while num_is_even:
        num_of_games = input("Please enter an odd number: ")
        num_is_even = is_even(num_of_games)

    return num_of_games

def get_user_choice() -> str:

        user_choice = input("Enter: \n1 for Rock \n2 for Paper \n3 for Scissors\n")

        is_valid = CHOICES.get(user_choice) ## look up the .get method for dictionaries
        while is_valid is None:
            user_choice = input("Please enter an integer from 1 to 3: ")
            is_valid = CHOICES.get(user_choice)

        return user_choice

''' ------------ HELPER FUNCTIONS ------------ '''

def play_round(user_input: str) -> Optional[bool]:
    '''Decide winner of the RPS round'''

    random_number = str(randint(1,3))
    computer_choice = CHOICES[random_number]

    user_choice = CHOICES[user_input]

    if ((user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")):
        return True
    elif (user_choice == computer_choice):
        return None
    else:
        return False

''' ------------ MAIN HANDLER ------------ '''

def play_game():

    num_of_games = get_num_of_games()

    # initialize players
    computer = Computer("Computer")
    user = User("You", num_of_games) ## can ask user for their name if you'd like

    # Keep looping until a player wins enough rounds
    while user.games_played < user.total_num_of_rounds:
        user_choice = get_user_choice()

        has_user_won = play_round(user_choice)

        if has_user_won is True:
            user.won_round()
        elif has_user_won is False:
            computer.won_round()
        else:
            user.tied_round()

        user.played_round()

    print(f"\nRounds played: {user.total_num_of_rounds}")
    print(f"Rounds Won: {user.wins}")
    print(f"Rounds Lost: {computer.wins}")
    print(f"Rounds Drawn: {user.draws}")

play_game()
