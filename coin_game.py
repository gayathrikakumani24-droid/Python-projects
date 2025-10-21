import random
print("===COIN FLIP GAME===")
print("*Guess heads or tails!*")
coin=["heads","tails"]
while True:
 guess=input("Enter your guess (heads/tails): ")
 if guess!="heads" and guess!="tails":
  print("Please enter 'heads' or 'tails'")
  continue  #it goes back to start of the loop
 flip=random.choice(coin)
 print(f"The coin shows:: {flip}")
 if(guess==flip):
  print("You Won!!!You guessed Correctly!")
 else:
  print("Sorry,wrong guess.Try again!")
 play=input("\nPlay again? (yes/no): ").lower()
 if play=="yes":
    continue
 else:
  print("GoodBye!!!")
  break
