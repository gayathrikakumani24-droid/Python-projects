import random
import time
def chatbot():
    greetings=["Hello there!","Hi Friend...","Hey! Nice to meet you"]
    farewells=["GoodBye!","See you Later!","See you Later..."]
    jokes=["Why don't scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break. Now it won't stop sending me beach wallpapers!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!", 
        "What do you call fake spaghetti? An impasta!","Why did the bicycle fall over? Because it was two-tired!"]
    facts=["Go!” is the shortest grammatically correct sentence in English","The original name for butterfly was 'flutterby'",
           "Porcupines can float","Apples float on water!","Owls can't move their eyeballs","The sunset on Mars appears blue.",
           "Hippopotamus produces pink milk.","Your skin is the largest body organ!","A day on Venus is longer than a year on venus"]
    bot_name="Chatbot"
    print(f"{bot_name} is starting up....")
    time.sleep(1)
    print(f"""
   Welcome to {bot_name}!
   I can chat about:
   'joke' - Hear a Funny Joke
   'fact' - Learn something new
   'color' - Favourite color
   'bye' - End our Chat
""")
    chatting=True
    user_name=input("What's your Name: ").title().strip()
    print(f"{bot_name}: Nice to meet you, {user_name}!How can I help you today?")
    while chatting:
        user_input=input("You: ").strip()
        if user_input in ["hi","hello","hey"]:
            print(f"{bot_name}: {random.choice(greetings)}")
        elif "joke" in user_input:
            print(f"{bot_name}: {random.choice(jokes)}")
        elif "fact" in user_input:
            print(f"{bot_name}: {random.choice(facts)}")
        elif "color" in user_input:
            print(f"{bot_name}: My favourite color is robot blue. What's yours?")
            color=input("You: ").strip()
            print(f"{bot_name}: {color} is a great color!")
        elif user_input in ["bye","GoodBye","exit","quit"]:
            print(f"{bot_name}: {random.choice(farewells)}")
            print(f"{bot_name}: It was fun chatting with you, {user_name}")
            chatting=False
        else:
            responses=["That's interesting!Tell me more.","I'm not sure.Can you try something else?",
                       "Hmm...Let's talk about something else.Try asking for a joke or fact",""
                       "Beep! Beep! My robot brain is processing...Try something else until then!!!"]
            print(f"{bot_name}: {random.choice(responses)}")
        
    
print("Thanks for chatting")
chatbot()