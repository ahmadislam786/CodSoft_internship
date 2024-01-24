#TASK-4 ROCK-PAPER-SCISSORS GAME

import random

def Play(player):
    choices = ['rock', 'scissors', 'paper']
    print('\n')
    print(f"\tWelcome {player} to Rock-Paper-Scissors Game!")
    user = input(f"{player},enter your choice (rock, scissors, paper):").lower()
    comp = random.choice(choices)
    
    while user not in choices:
        print("Invalid choice: please choose from the following")
        user = input(f"{player},Enter your choice (rock, scissors, paper):").lower()
    
    if user == comp:
        result=("Match Tie")
    elif (user == 'rock' and comp == 'scissors') or (user == 'scissors' and comp == 'paper') or (user == 'paper' and comp == 'rock'):
        result = f"Wow {player},You won!"
    else:
        result = f"{player},You lose!"

    print(f"\n{player} choice: {user.capitalize()}")
    print(f"Computer's choice: {comp.capitalize()}")
    print(result)
    return result

def main():
    User_Score = 0
    Comp_Score = 0
    player=input("Enter your Name:").capitalize()
    while True:
        result = Play(player)
        
        if "won" in result:
            User_Score += 1
        elif "lose" in result:
            Comp_Score += 1
        
        print(f"\nScores - {player}: {User_Score}, Computer: {Comp_Score}")
        
        again = input("Do you want to play again? (yes/no):").lower()
        if "no" in again:
            print("Thanks you!")
            break

if __name__ == "__main__":
    main()
