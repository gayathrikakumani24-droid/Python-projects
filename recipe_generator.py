import random
print("===RANDOM RECIPE GENERATOR===")
recipes=["Paneer butter masala with paratha","Bryani and sherva","Upma","Pongal and Sambar","Noodles","Manchuria","Veg Fried Rice and Manchurian noodles","Egg Fried Rice","Black Forest Cake","Red velvet Cake","Gulab Jamun",
"Double ka Meetha"]
while True:
  choice=random.choice(recipes)
  print(f"Suggested Random Recipe: {choice}")
  again=input("Generate another recipe? (yes/no): ")
  if(again=="yes"):
    continue
  else:
    break
