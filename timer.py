import time
print("===COUNTDOWN TIMER===")
print("Count down from your chosen seconds")
while True:
    seconds=int(input("Enter seconds to countdown from: "))
    print(f"Starting countdown from {seconds} seconds!")
    for i in range(seconds,0,-1):
        print(f"{i} seconds remaining....")
        time.sleep(1)

    print("\nCountdown Completed")
    again=input("Start another countdown???(yes/no): ").lower()
    if(again=="yes"):
        continue
    else:
        print("GoodBye!!!")
        break