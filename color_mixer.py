color_mixes={
    ("red","blue"):"purple",
    ("red","yellow"):"orange",
    ("blue","yellow"):"green",
    ("blue","green"):"teal",
    ("white","red"):"pink",
    ("red","green"):"brown"
}
while True:
    color1=input("\nEnter first color: ").lower()
    color2=input("\nEnter second color: ").lower()
    mix=None
    if (color1,color2) in color_mixes:
        mix=color_mixes[(color1,color2)]
    if mix:
        print(f"When you mix {color1} and {color2},you get {mix}")
    else:
        print("Don't know what those colors make when mixed.")
    again=input("Play Again?: ").lower()
    if not again.startswith("y"):
        break