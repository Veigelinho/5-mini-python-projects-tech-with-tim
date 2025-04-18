import random
import re # regular expression

print("""Welcome to Rock, Paper, Scissors.
Do you want to play?""")

has_confirmed = False
wants_to_play = False

while not has_confirmed:
    player_confirmation = input("""Please type Y for Yes or N for No
> """).lower()

    if player_confirmation == "y" or player_confirmation == "n":
        
        if player_confirmation == "y":
            print("Cool! Let's start playing!")
            has_confirmed = True
            wants_to_play = True
        
        elif player_confirmation == "n":
            print("Bummer. See you next time!")
            break
        
    else:
        print("Invalid entry.")
        continue
    
       

player_score = 0
computer_score = 0

while wants_to_play:
    score = f"You {player_score}:{computer_score} Computer"
    current_score = f"Current score: {score}"
    print(current_score)

    player_choice = input("""Press R for Rock, P for Paper or S for Scissors, or e to end the game.
> """).lower()
    


    if player_choice in ["r", "p", "s"]:
        computer_choice = random.randint(1,3)
        
        if computer_choice == 1:
            computer_choice = "r"
            
            if player_choice == computer_choice:
                print("Draw. You both picked Rock.")
            elif player_choice == "p":
                print("You won! The computer chose rock.")
                player_score +=1
            else:
                print("You lost! The computer chose rock.")
                computer_score +=1
        
        elif computer_choice == 2:
            computer_choice = "p"
            
            if player_choice == computer_choice:
                print("Draw. You both picked Paper.")
            elif player_choice == "s":
                print("You won! The computer chose Paper.")
                player_score +=1
            else:
                print("You lost! The computer chose Paper.")
                computer_score +=1
        
        else:
            computer_choice = "s"
            
            if player_choice == computer_choice:
                print("Draw. You both picked Scissors.")
            elif player_choice == "r":
                print("You won! The computer chose Scissors.")
                player_score +=1
            else:
                print("You lost! The computer chose Scissors.")
                computer_score +=1
    
    elif player_choice in "e":
        wants_to_play = False
        
        print("Wow, what a game!")
        final_score = f"Final score: {score}"


        if player_score == computer_score:
            print("It's a draw!")
        
        elif player_score > computer_score:
            print("Hats off! You won against the computer!")
        
        else:
            print("Is the computer smarter than you? You lost!")
        
        print(f"{final_score}")

    else:
        print("Invalid input.")