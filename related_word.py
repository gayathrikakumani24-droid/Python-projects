import random
import time
print("===WORD ASSOCIATION GAME===")
print("Respond with a related word quickly!")
word_pairs={
    "sky":["blue","cloud","bird","fly","sun"],
    "water":["drink","ocean","rain","swim","fish","river"],
    "food":["eat","cook","tasty","hungry","meal","restaurant"],
    "music":["song","dance","listen","band","rhythm","instruments","happy"],
    "book":["read","story","knowledge","page","author","library","price"],
    "tree":["leaf","green","forest","wood","shade","food","shelter"],
    "car":["drive","road","tyres","travel","speed"],
    "dog":["pet","bark","walk","loyal","puppy"]
}
score=0
rounds=0
while True:
    #select a random word
    prompt=random.choice(list(word_pairs.keys()))
    related_words=word_pairs[prompt]

    print(f"Prompt word: {prompt.upper()}")
    print("Quick!Type a word related to this prompt!")
    #Time the player's response
    start_time=time.time()
    print(start_time)
    #if user enters " hello ",it will be converted to "hello"
    response=input(">").lower().strip()
    response_time=time.time()-start_time
    print("response time",response_time)
    
    if response in related_words:
        points=max(1,5-int(response_time))
        score+=points
        print(f"Good association! +{points} (answered in {response_time:.1f}s)")
    else:
        print(f"No a common Association.Related words include: {",".join(related_words)}")
    rounds+=1
    print(f"Score: {score}/{rounds*5} possible points")
    if input("Play again? (yes/no): ").lower().stratswith("n"):
        print("GoodBye")
        break
