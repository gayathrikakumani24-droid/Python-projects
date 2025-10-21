import random
print("Welcome to Number Guessing Game!!!")
print("Guess the Number between  1 to 100 within 10 attempts to win the Game")
playing=True
while playing:
    secret_number=random.randint(1,100)
    attempts=0
    max_attempts=10
    game_over=False
    while attempts<max_attempts and not game_over:
        try:
            guess=int(input(f"Attempt {attempts+1}/{max_attempts}.Enter your guess: "))
        except ValueError:
            print("Please Enter a valid Number")
            continue
        attempts+=1
        if guess<secret_number:
            print("---Too Low! Try a Higher Number---")
        elif guess>secret_number:
            print("---Too High! Try a Lower Number---")
        else:
            print(f"Congrats!!!You have guessed the Number {secret_number} in {attempts} attempts Correctly!!")
            game_over=True
        if attempts<max_attempts and not game_over:
            print(f"You have {max_attempts-attempts} attempts left")
    if not game_over:
            print(f"Game_over! The number was {secret_number}")
    again=input("Play Again?: ").lower()
    if(again=="yes"):
           print("New Game Starting....")
           continue
    else:
           print("Good Bye!!!")
           break

