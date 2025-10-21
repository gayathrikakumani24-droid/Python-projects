import random
import time
def get_user_choice():
    while True:
        print("Make your choice: ")
        print("1. Rock")
        print("2. Papers")
        print("3. Scissors")
        try:
            choice=int(input("Enter your choice: "))
            if 1<=choice<=3:
                return choice
            else:
                print("Enter a valid number")
        except ValueError:
            print("Enter a valid choice")
def get_computer_choice():
    return random.random

def convert_choice_to_text(choice):
    options={1:"Rock",2:"Paper",3:"Scissors"}
    return options[choice]

def display_welcome():
    print("\n===ROCK PAPER SCISSORS===")
    print("\nRules: ")
    print("Rock crushes Scissors")
    print("Scissors cuts paper")
    print("Paper covers rock")
    print("First to win 3 rounds is the champion")
    print("\n-------------------------")
def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "tie"
    elif(user_choice==1 and computer_choice==3) or (user_choice==3 and computer_choice==2) or(user_choice==2 and computer_choice==1):
      return "user"
    else:
        return "computer"
def display_round_result(user_choice,computer_choice,result):
    user_text=convert_choice_to_text(user_choice)
    computer_text=convert_choice_to_text(computer_choice)
    print(f"\nYou chose: {user_text}")
    print("\nComputer is choosing")
    for i in range(3):
        print(",")
        time.sleep(0.5)
    print(f"Computer chose: {computer_text}")
    if result=="tie":
        print("It's a Tie")
    elif result=="user":
        print("You win this rounds!")
    else:
        print("Computer wins the round!")
def play_game():
    '''Main game function'''
    display_welcome()
    user_score=0
    computer_score=0
    target_score=3
    round_num=1
    no_winners= user_score<target_score and computer_score<target_score
    while no_winners:
        print(f"\n===ROUND {round_num}===")
        print(f"Score: You:{user_score} -Computer: {computer_score}")

        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        result=determine_winner(user_choice,computer_choice)
        display_round_result(user_choice,computer_choice,result)

        if result=="user":
            user_score+=1
        elif result=="computer":
            computer_score+=1
        round_num+=1
    print("\n===GAME OVER===")
    print(f"Final Score: You {user_score}-{computer_score} Computer")
    if user_score>computer_score:
        print("Congrats!You are the Champion")
    else:
        print("Better luck next time!The computer wins the game.")
    again=input("Play again? (yes/no): ")
    if(again=="yes"):
         play_game()
    else:
         print("Thanks for playing!!!")
        

play_game()
