import random

print("Welcome to stone paper scissor !!")


def Tic_Tac_Toe():
    options = ["r","p","s"]
    computer_choice = random.randint(0,2)
    computer_pick = options[computer_choice]
    computer_score = 0
    user_score = 0
    choice = input ("Do you want to play? Enter Yes or No.\n").lower()
    
    
    if choice == "yes":
        # Enter a scoreboard

        while True:
            user_guess = input("Choose between Rock(r),Paper(p),Scissor(s).\n").lower()
            if user_guess == computer_pick:
                print("It's a tie!!")
            elif user_guess == "r" and computer_pick == "p":
                print("You lose! :(")
                computer_score += 1
            elif user_guess == "p" and computer_pick == "s":
                print("You lose! :(")
                computer_score += 1
            elif user_guess == "s" and computer_pick == "r":
                print("You lose! :(")
                computer_score += 1
            elif user_guess == "p" and computer_pick == "r":
                print("You Won! :)")
                user_score += 1
                break
            elif user_guess == "s" and computer_pick == "p":
                print("You Won! :)")
                user_score += 1
                break
            elif user_guess == "r" and computer_pick == "s":
                print("You Won! :)")
                user_score += 1
                break
    elif(choice == "no"):
        quit()
    else:
        print("Enter a valid input!!")
    print (f"Your score- {user_score}")
    print(f"Computer score - {computer_score}")
Tic_Tac_Toe()