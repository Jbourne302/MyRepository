
import random

def Rock_Paper_Sissors_Winner(user_input):
    
    # This function will decide the winner of a Rock, Paper, Sissors game
    
    # Generate a random number
    random_number = random.randint(1,300)
    
    # Takes the users input as a number, and interprets that as Rock,Paper, or Sissors
    if user_input == 1:
        user_choice = "Rock"
    elif user_input == 2:
        user_choice = "Paper"
    else: 
        user_choice = "Sissors" 
    
    # Generate a random number to go up against the user
    if random_number %3 == 0:
        computer_choice = "Rock"
    elif random_number %3 == 1:
        computer_choice = "Paper"
    else: 
        computer_choice = "Sissors"
        
    # Return "Win","Lose","Draw" depending on the outcome
    if ((user_choice == "Rock" and computer_choice == "Sissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or 
        (user_choice == "Sissors" and computer_choice == "Paper")):
        return "Win"
    elif (user_choice == computer_choice):
        return "Draw"
    else:
        return "Lose"

#==============================================================================

def Rock_Paper_Sissors():
    
    # Decide the amound of games the user wants to play the best out of
    number_of_games = int(input("How many games do you want to play?: "))
    
    # The number must be an odd number to detrmine a winner
    while(number_of_games %2 != 1):
        number_of_games = int(input("Please enter an odd number: "))
    
    # Keep track of required amount of wins needed for game over
    rounds = int((number_of_games + 1)/2)
    
    # Keep track of the rounds the user wins and looses
    rounds_won = 0
    rounds_lost = 0
    rounds_drawn = 0
    
    # Keep looping until a player wins enough rounds
    while rounds_won != rounds and rounds_lost != rounds:
        
        # Take the users choice of Rock, Paper, Sissors in the form of 1,2,3 respeectivley
        users_choice = int(input("Enter: \n1 for Rock \n2 for Paper \n3 for Sissors\n"))
        
        # Make sure the user enters an eacceptable input
        while(users_choice != 1 and users_choice != 2 and users_choice != 3):
            users_choice = int(input("Please enter an integer from 1 to 3: "))
            
        # Returns 1 if the user wins a round and 0 otherwise
        if Rock_Paper_Sissors_Winner(users_choice) == "Win":
            print("You won this round")
            rounds_won += 1
        elif Rock_Paper_Sissors_Winner(users_choice) == "Lose":
            print("You lost this round")
            rounds_lost += 1
        else:
            print("Its a draw")
            rounds_drawn += 1
            
    print("\nRounds played: ",(rounds_won + rounds_lost + rounds_drawn), "\nRounds Won: ",rounds_won, "\nRounds Lost: ",rounds_lost, "\nRounds Drawn: ",rounds_drawn )
#==============================================================================           
        
        
Rock_Paper_Sissors()
