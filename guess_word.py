import random
print("===WORD SCRAMBLE GAME===")
print("Guess the Scrambled Word")
words={"happy":"An expression","python":"A programming language","learn":"a task","computer":"A Machine","education":"taught in school","fun":"we enjoy","enjoy":"living the moment","coffee":"a beverage","trip":"substitute for vacation","exercise":"physical work","joy":"substitute for happy"}
while True:
    original_word=random.choice(list(words.keys()))
    letters=list(original_word)
    random.shuffle(letters)
    scrambled="".join(letters)
    print(f"Scrambled Word: {scrambled}")
    print(f"HINT: {words[original_word]}")
    guess=input("What's the word: ").lower()
    if(guess==original_word):
        print("Congrats!You won!")
    else:
        print(f"Sorry!The word was {original_word}")
    again=input("Play Again?: ").lower()
    if(again=="yes"):
        continue
    else:
        print("Thank you!!!")
        break