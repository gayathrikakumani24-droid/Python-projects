import random
print("***GUESS THE WORD***")
words={"food":["bhelpuri","panipuri","vadapav","pavbhaji","pizza","sandwich","burger","cutlet","samosa"],
       "cities":["Hyderabad","Chennai","Kerala","Mumbai","Delhi","Kolkata","Kashmir","Rajasthan","Amaravathi"],
       "musical instruments":["flute","guitar","sitar","drums","violin","piano","veena","harmony"]}
while True:
  category=input("Select a category to guess related word (food/cities/musical instruments): ").lower()
  if(category=="food"):
    comp_choice=random.choice(words["food"])
  elif(category=="cities"):
    comp_choice=random.choice(words["cities"])
    print(comp_choice)
  elif(category=="music"):
    comp_choice=random.choice(words["music"])
  else:
    print("category not found")
    continue
  user_choice=input().lower()
  for i in range(len(comp_choice)):
      if(user_choice==comp_choice[i]):
        print(user_choice)
      else:
        print("_",end="")