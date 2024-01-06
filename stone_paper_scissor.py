import random

def game(comp, you):

    if comp == you:
        print("The Game is Tie")

    elif comp == "s":
        if you == "sc":
            print("You Lose")
        elif you == "p":
            print("You Won") 

    elif comp == "p":
        if you == "s":
            print("You Lose")
        elif you == "sc":
            print("You Win")
            
    elif comp == "sc":
        if you == "s":
            print("You Won")
        elif you == "p":
            print("You Lose")

print("Computer's turn: stone(s) paper(p) or scissor(sc)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "p"
elif randNo ==3:
    comp = "sc"

you = input("Your turn - stone(s) paper(p) scissor(sc) ?")

game(comp, you)