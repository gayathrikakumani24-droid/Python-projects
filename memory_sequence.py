import random
import time
import os
def clear_screen():
    '''Clear the screen'''
    os.system("cls" if os.name=="nt" else "clear")
print("===MEMORY SEQUENCE GAME===")
print("Remember the sequence and type it back")
print("Rules:")
print("-- Watch as numbers appear one by one")
print("-- After the sequence is shown,type it back in order seperated by spaces")
print("--Each round adds one more number to remember")
print("--How far can you go?")
input("Press Enter to start...")
sequence=[]
current_round=1
game_over=False
while not game_over:
    sequence.append(random.randint(1,9))
    clear_screen()
    print(f"\n===Round {current_round}===")
    print(f"Remember thIS sequence of {len(sequence)} numbers: ")
    for number in sequence:
     time.sleep(0.7)
     print(f"\n{number}")
     time.sleep(0.7)
     clear_screen()
    print("Now repeat the sequence by typing numbers seperated by spaces")
    player_answer=input("> ")
    try:
     player_sequence=[int(num) for num in player_answer.split()]
    except ValueError:
     print("Please Enter Numbers only!")
     game_over=True
     continue
    if player_sequence==sequence:
     print(f"Congrats!You remembered all {len(sequence)} numbers!")
     current_round+=1
     time.sleep(2)
    else:
     print(f"Game Over!!!You remembered {current_round-1} numbers")
     print(f"The current sequence was {" ".join(str(num) for num in sequence)}")
     game_over=True
     if game_over:
       again=input("Play again? (yes/no): ")
       if(again=="yes"):
         sequence=[]
         current_round=1
         game_over=False
         continue
       else:
         print("Thanks for playing!!!")
         break
       
       

